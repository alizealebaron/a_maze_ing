# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  generation.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 15:33:35 by alebaron        #+#    #+#               #
#  Updated: 2026/02/13 12:31:35 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from .maze import Maze, Cell, MazeError
from random import randint
import random
from rich.live import Live


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
    exit = config["EXIT"]

    def get_unvisited_neibourg(coord: tuple, visited: list) -> list:
        lst_unvisited_neibourg = []

        x, y = coord

        neibourg_N = (x, y-1)
        neibourg_S = (x, y+1)
        neibourg_O = (x-1, y)
        neibourg_E = (x+1, y)

        lst_neibourg = [neibourg_N, neibourg_S, neibourg_O, neibourg_E]

        for people in lst_neibourg:
            x, y = people

            try:
                if (maze.maze[people] == Cell.STRICT):
                    continue

                if (people not in visited and x >= 0 and y >= 0 and
                x < config["WIDTH"] and y < config["WIDTH"]):
                    lst_unvisited_neibourg.append(people)
            except Exception:
                pass

        return lst_unvisited_neibourg

    def kill(cell: tuple[int, int]):

        visited_cell.append(cell)
        un_neibourg = get_unvisited_neibourg(cell, visited_cell)

        while (len(un_neibourg) > 0):

            x, y = cell

            # Randomize a direction
            direction = randint(0, (len(un_neibourg) - 1))
            direction = un_neibourg.pop(direction)

            un_neibourg = get_unvisited_neibourg(direction, visited_cell)

            # Change the cell in path

            if (maze.is_editable(direction)):
                maze.change_cell(direction, Cell.BLANK)

            # Make sure that there is wall

            for neibourg in un_neibourg:
                visited_cell.append(neibourg)

            visited_cell.append(direction)

    def hunt(visited_cell: list) -> tuple[int, int] | None:

        for y in range(0, width):
            for x in range(0, height):
                cell = (x, y)
                unvisited = get_unvisited_neibourg(cell, visited_cell)

                if (len(unvisited) > 0):
                    next_cell = unvisited[0]

                    if (maze.is_editable(cell)):
                        maze.change_cell(cell, Cell.BLANK)

                    return next_cell
        return None

    # Get the seed
    try:
        random.seed(config["SEED"])
    except Exception:
        pass

    # Initialization of visited cells

    visited_cell = [exit]

    # Begin of hunt

    cell = config["ENTRY"]

    with Live("", refresh_per_second=1) as live:

        while (cell is not None):
            kill(cell)
            cell = hunt(visited_cell)
            live.update(maze.show_maze())
