# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  generation.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 15:33:35 by alebaron        #+#    #+#               #
#  Updated: 2026/02/13 16:11:07 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from .maze import Maze, Cell, MazeError
from random import randint
import random
from rich.live import Live
from rich.text import Text
import time


# +-------------------------------------------------------------------------+
# |                              Side Winder                                |
# +-------------------------------------------------------------------------+

def side_winder(maze: Maze) -> None:
    for y in range(0, maze.height, 2):
        for x in range(0, maze.width, 2):
            try:
                maze.change_cell((x, y), Cell.BLANK)
            except MazeError:
                pass

    for y in range(0, maze.height - 1, 2):
        xvalmax = randint(0, int(maze.width/3))
        for x in range(1, maze.width - 1, 2):
            try:
                if y == 0:
                    if x >= xvalmax:
                        maze.change_cell((x + 1, y + 1), Cell.BLANK)
                        xvalmax = x + randint(1, int(maze.width/3))
                    maze.change_cell((x, y), Cell.BLANK)
                elif x >= xvalmax and y <= maze.height - 2:
                    maze.change_cell((x + 1, y + 1), Cell.BLANK)
                    xvalmax = x + randint(1, int(maze.width/3))
                else:
                    maze.change_cell((x, y), Cell.BLANK)
            except MazeError:
                pass


# +-------------------------------------------------------------------------+
# |                             Hunt and kill                               |
# +-------------------------------------------------------------------------+


def hunt_and_kill(maze: Maze, config: dict) -> None:

    width = config["WIDTH"]
    height = config["HEIGHT"]

    def get_neighbors(coord: tuple, visited: set, is_unvisited: bool) -> list:

        x, y = coord
        # Possible direction
        directions = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]
        valid_neighbors = []

        for nx, ny in directions:
            if 0 <= nx < width and 0 <= ny < height:

                if is_unvisited:
                    if (nx, ny) not in visited and maze.maze[(nx, ny)] != Cell.STRICT:
                        valid_neighbors.append((nx, ny))

                else:
                    if (nx, ny) in visited:
                        valid_neighbors.append((nx, ny))

        return valid_neighbors

    def try_change_cell(maze: Maze, cell: tuple[int, int], live: Live):
        if (maze.is_editable(cell)):
            maze.change_cell(cell, Cell.BLANK)
            live.update(Text.from_ansi(maze.show_maze()))
            time.sleep(0.05)

    def break_wall_between(cell1: tuple, cell2: tuple, live: Live):
        x1, y1 = cell1
        x2, y2 = cell2

        # To break the wall, we need the cell between empty
        wall_cell = ((x1 + x2) // 2, (y1 + y2) // 2)

        # And than we can change our path
        try_change_cell(maze, wall_cell, live)
        try_change_cell(maze, cell2, live)

    def kill(current_cell: tuple[int, int], visited_cell: set, live: Live):

        visited_cell.add(current_cell)

        while True:
            neighbors = get_neighbors(current_cell, visited_cell, True)
            if not neighbors:
                break

            # Choose a random destination
            next_cell = random.choice(neighbors)

            # Open a path between several path
            break_wall_between(current_cell, next_cell, live)

            # Move on the next
            visited_cell.add(next_cell)
            current_cell = next_cell

    def hunt(visited_cell, live):

        # Calculing parity of the algorithm

        start_x, start_y = config["ENTRY"]
        offset_x = start_x % 2
        offset_y = start_y % 2

        for y in range(offset_y, height, 2):
            for x in range(offset_x, width, 2):
                cell = (x, y)

                if cell not in visited_cell and maze.maze[cell] != Cell.STRICT:

                    neighbors = get_neighbors(cell, visited_cell, False)
                    if neighbors:
                        v_neigh = random.choice(neighbors)
                        break_wall_between(v_neigh, cell, live)
                        return cell
        return None

    # Get the seed
    try:
        random.seed(config["SEED"])
    except Exception:
        pass

    # Initialization of visited cells

    visited_cell = {config["ENTRY"]}
    cell = config["ENTRY"]

    with Live("", refresh_per_second=25) as live:

        while (cell is not None):
            kill(cell, visited_cell, live)
            cell = hunt(visited_cell, live)

            maze_render = Text.from_ansi(maze.show_maze())
            live.update(maze_render)
