# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  resolution.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 12:39:18 by tcolson         #+#    #+#               #
#  Updated: 2026/02/24 11:23:42 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from .maze import Maze, Cell
from rich.live import Live
from rich.text import Text
from time import sleep
from typing import Optional, Any


# +-------------------------------------------------------------------------+
# |                               Functions                                 |
# +-------------------------------------------------------------------------+


def resolution(maze: Maze, config: dict[str, Any]) -> str:
    """
    Find the shortest path through the maze using a recursive backtracking
    algorithm.

    This function explores the maze starting from the entry point defined in
    the config.
    It can visually animate the solving process using the 'Live' display if
    enabled.
    The exploration order is optimized by prioritizing directions that lead
    toward the exit coordinates.

    Args:
        maze (Maze): The maze object containing the grid and cell manipulation
        methods.
        config (dict): A configuration dictionary containing:
            - "WIDTH" (int): Grid width.
            - "HEIGHT" (int): Grid height.
            - "EXIT" (tuple): Exit coordinates (x, y).
            - "ENTRY" (tuple): Starting coordinates (x, y).
            - "HIDE" (bool): If False, animates the solving process.

    Returns:
        str: A string of directions (e.g., "NSSWEE") representing the path from
             start to finish.
    """

    width = config["WIDTH"]
    height = config["HEIGHT"]
    path = ""

    def explore_cell(cell: tuple[int, int], live: Optional[Live]) -> None:
        """
        Mark a cell as part of the current path and refresh the UI.

        Args:
            cell (tuple): The (x, y) coordinates to mark.
            live (Optional[Live]): The Live display object for
                real-time rendering.
        """
        maze.change_cell(cell, Cell.SOLVE)
        if live:
            live.update(Text.from_ansi(maze.show_maze()))
            sleep(0.05)

    def get_directions(pos: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Calculate and sort possible movement directions based on proximity
        to the exit.

        Heuristic: Prioritizes movements that reduce the distance to the
        target (EXIT) to improve search efficiency.

        Args:
            pos (tuple): Current (x, y) position.

        Returns:
            list[tuple]: A list of adjacent (x, y) coordinates sorted by
            priority.
        """
        x, y = pos
        endx, endy = config["EXIT"]
        diffx = endx - x
        diffy = endy - y
        directions = []
        if abs(diffx) >= abs(diffy):
            if diffx > 0:
                directions.append((x+1, y))
                if diffy > 0:
                    directions.append((x, y+1))
                    directions.append((x, y-1))
                    directions.append((x-1, y))
                else:
                    directions.append((x, y-1))
                    directions.append((x, y+1))
                    directions.append((x-1, y))
            else:
                directions.append((x-1, y))
                if diffy > 0:
                    directions.append((x, y+1))
                    directions.append((x, y-1))
                    directions.append((x+1, y))
                else:
                    directions.append((x, y-1))
                    directions.append((x, y+1))
                    directions.append((x+1, y))
        else:
            if diffy > 0:
                directions.append((x, y+1))
                if diffx > 0:
                    directions.append((x+1, y))
                    directions.append((x-1, y))
                    directions.append((x, y-1))
                else:
                    directions.append((x-1, y))
                    directions.append((x+1, y))
                    directions.append((x, y-1))
            else:
                directions.append((x, y-1))
                if diffx >= 0:
                    directions.append((x+1, y))
                    directions.append((x-1, y))
                    directions.append((x, y+1))
                else:
                    directions.append((x-1, y))
                    directions.append((x+1, y))
                    directions.append((x, y+1))
        return directions

    def solve(pos: tuple[int, int], live: Optional[Live]) -> bool:
        """
        Recursively explore the maze to find the exit.

        This internal helper uses backtracking: if a path leads to a dead end,
        it reverts the cell state and tries the next available direction.

        Args:
            pos (tuple): Current (x, y) position.
            live (Optional[Live]): The Live display object for real-time
            rendering.

        Returns:
            bool: True if the exit was found from this branch, False otherwise.
        """
        x, y = pos
        directions = get_directions(pos)
        nonlocal path

        for nx, ny in directions:
            newpos = (nx, ny)

            if nx > width - 1 or nx < 0 or ny > height - 1 or ny < 0:
                pass
            else:
                if maze.maze[newpos] == Cell.EXIT:
                    if newpos == (x, y-1):
                        path += "N"
                    if newpos == (x, y+1):
                        path += "S"
                    if newpos == (x-1, y):
                        path += "W"
                    if newpos == (x+1, y):
                        path += "E"
                    return True
                elif maze.maze[newpos] == Cell.BLANK:
                    explore_cell(newpos, live)
                    res = solve(newpos, live)
                    if res:
                        if newpos == (x, y-1):
                            path += "N"
                        if newpos == (x, y+1):
                            path += "S"
                        if newpos == (x-1, y):
                            path += "W"
                        if newpos == (x+1, y):
                            path += "E"
                        return True
                    else:
                        maze.change_cell(newpos, Cell.BLANK)
        return False

    # Start to solve, stop when finding the exit

    if not config["HIDE"]:
        with Live("", refresh_per_second=25) as live:

            solve(config["ENTRY"], live)

            maze_render = Text.from_ansi(maze.show_maze())
            live.update(maze_render)
    else:
        solve(config["ENTRY"], None)
        maze.clean_path()
    return path[::-1]
