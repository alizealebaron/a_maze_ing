# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  generation.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 15:33:35 by alebaron        #+#    #+#               #
#  Updated: 2026/02/24 11:27:08 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from .maze import Maze, Cell
import random
from rich.live import Live
from rich.text import Text
import time
from typing import Any


# +-------------------------------------------------------------------------+
# |                             Hunt and kill                               |
# +-------------------------------------------------------------------------+


def hunt_and_kill(maze: Maze, config: dict[str, Any]) -> None:
    """
    Generates a maze using the Hunt-and-Kill algorithm with visual updates.

    The algorithm operates in two alternating phases:
    1. Kill Phase: A random walk from the current cell, carving a path into
       unvisited cells until it reaches a dead end.
    2. Hunt Phase: Scans the grid for an unvisited cell that is adjacent
       to a visited one.
       If found, it connects them and starts a new Kill phase.

    This specific implementation includes parity checks to ensure the maze
    integrity based on the entry/exit coordinates and a "perfect" maze flag.

    Args:
        maze (Maze): The maze object to be modified. It should provide methods
            like `is_editable`, `change_cell`, and `show_maze`.
        config (dict): Configuration dictionary containing:
            - "WIDTH" (int): Width of the maze.
            - "HEIGHT" (int): Height of the maze.
            - "EXIT" (tuple): (x, y) coordinates of the exit.
            - "ENTRY" (tuple): (x, y) coordinates of the starting cell.
            - "PERFECT" (bool): Whether to enforce a perfect maze structure.
            - "SEED" (int, optional): Seed for the random number generator.

    Note:
        - The function uses a `Live` object for real-time terminal rendering.
        - Parity logic is used to handle specific constraints where the exit
          might be blocked or require special pathfinding rules.
        - Internal helper functions (`kill`, `hunt`, `get_neighbors`, etc.)
          manage the state and movement within the grid.

    Returns:
        None: The function modifies the `maze` object in-place.
    """

    width = config["WIDTH"]
    height = config["HEIGHT"]
    exit = config["EXIT"]
    cell = config["ENTRY"]
    perfect = config["PERFECT"]

    ex, ey = exit
    lock_coord = [(ex-1, ey-1), (ex+1, ey+1)]

    def is_parity_ok() -> bool:

        x, y = cell

        par_x = x % 2 == 0
        par_y = y % 2 == 0

        par_ex = ex % 2 == 0
        par_ey = ey % 2 == 0

        # print(f"x = {par_x} | y = {par_y} | ex = {par_ex} | ey = {par_ey}")

        if (par_x is True and par_y is False and par_ey is True):
            return False
        elif (par_x is False and par_y is True and par_ex is True):
            return False
        elif (par_x is False and par_y is False and par_ey is False):
            # print("2")
            return False
        elif (par_x is True and par_y is True and par_ex is False):
            # print("3")
            return False
        else:
            return True

    # print(f"Parity : {is_parity_ok()} Perfect : {perfect}")
    parity = (is_parity_ok() is False) and perfect
    # print(f"is_parity_ok() is False = {is_parity_ok() is False}")
    # print(f"Total : {parity}")

    def get_neighbors(coord: tuple[int, int], visited: set[tuple[int, int]],
                      is_unvisited: bool) -> list[tuple[int, int]]:
        x, y = coord
        ex, ey = exit

        # Possible direction
        directions = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]
        valid_neighbors = []

        parity = (is_parity_ok() is False) and perfect

        # Lock some direction to avoid non perfect path

        for nx, ny in directions:

            avg_x = ((nx + x) // 2)
            avg_y = ((ny + y) // 2)
            if 0 <= nx < width and 0 <= ny < height:

                if (parity is True):
                    # Special case: The exit is in the lower right corner.
                    if (((ex == 0 and ey == 0) or
                         (ex == width - 1 and ey == height - 1)) is False):

                        if (nx, ny) in lock_coord:
                            continue

                        if (avg_x, avg_y) in lock_coord:
                            continue

                        if abs(nx - ex) <= 1 and abs(ny - ey) <= 1:
                            if (nx, ny) != (ex, ey):
                                continue

                if is_unvisited:
                    if (nx, ny) not in visited and\
                     maze.maze[(nx, ny)] != Cell.STRICT and\
                     maze.maze[(avg_x, avg_y)] != Cell.STRICT:
                        valid_neighbors.append((nx, ny))

                else:
                    if (nx, ny) in visited and\
                     maze.maze[(avg_x, avg_y)] != Cell.STRICT:
                        valid_neighbors.append((nx, ny))

        return valid_neighbors

    def try_change_cell(maze: Maze, cell: tuple[int, int], live: Live) -> None:
        if (maze.is_editable(cell)):
            maze.change_cell(cell, Cell.BLANK)
            live.update(Text.from_ansi(maze.show_maze()))
            time.sleep(0.02)

    def break_wall_between(cell1: tuple[int, int],
                           cell2: tuple[int, int], live: Live) -> None:
        x1, y1 = cell1
        x2, y2 = cell2

        # To break the wall, we need the cell between empty
        wall_cell = ((x1 + x2) // 2, (y1 + y2) // 2)

        # And than we can change our path
        try_change_cell(maze, wall_cell, live)
        try_change_cell(maze, cell2, live)

    def exit_connected(maze: Maze, config: dict[str, Any],
                       visited_cell: set[tuple[int, int]], live: Live) -> None:
        exit_node = config["EXIT"]
        x, y = exit_node
        direc = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]

        neighbors = []

        for nx, ny in direc:
            avg_x = ((nx + x) // 2)
            avg_y = ((ny + y) // 2)
            try:
                if maze.maze[(nx, ny)] != Cell.BLANK:
                    continue
                if maze.maze[(avg_x, avg_y)] == Cell.BLANK:
                    return
                if maze.maze[(avg_x, avg_y)] != Cell.STRICT:
                    neighbors.append((nx, ny))
            except Exception:
                pass

        if not neighbors:
            directions: dict[tuple[int, int], list[tuple[int, int]]] = {
                (x+1, y+1): [(x+1, y), (x, y+1)],
                (x+1, y-1): [(x+1, y), (x, y-1)],
                (x-1, y+1): [(x-1, y), (x, y+1)],
                (x-1, y-1): [(x-1, y), (x, y-1)],
            }

            for direction, _ in directions.items():
                try:
                    if (maze.maze[direction]) != Cell.STRICT and\
                       (maze.maze[direction]) != Cell.WALL:
                        random_dir = random.choice(directions[direction])
                        maze.change_cell(random_dir, Cell.BLANK)
                        return
                except Exception:
                    pass
        else:
            v_neigh = random.choice(neighbors)
            break_wall_between(v_neigh, exit_node, live)
            visited_cell.add(exit_node)

    def is_exit_connected(maze: Maze, exit: tuple[int, int]) -> bool:
        x, y = exit
        directions = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

        for nx, ny in directions:
            try:
                if maze.maze[(nx, ny)] == Cell.BLANK:
                    return True
            except Exception:
                pass

        return False

    def kill(current_cell: tuple[int, int],
             visited_cell: set[tuple[int, int]], live: Live) -> None:

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

    def hunt(visited_cell: set[tuple[int, int]],
             live: Live) -> tuple[int, int] | None:

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
        seed = random.randint(0, 314159265358979)
        config["RANDOM_SEED"] = seed
        random.seed(config["RANDOM_SEED"])

    # Initialization of visited cells
    visited_cell = set()

    if (parity is True):
        visited_cell.add(exit)

        # Special case: The exit is in the lower right corner.
        if (((ex == 0 and ey == 0) or
             (ex == width - 1 and ey == height - 1)) is False):
            visited_cell.add(lock_coord[0])
            visited_cell.add(lock_coord[1])

    with Live("", refresh_per_second=25) as live:

        while (cell is not None):
            kill(cell, visited_cell, live)
            cell = hunt(visited_cell, live)

            maze_render = Text.from_ansi(maze.show_maze())
            live.update(maze_render)

        if not is_exit_connected(maze, exit):
            exit_connected(maze, config, visited_cell, live)
        live.update(Text.from_ansi(maze.show_maze()))
