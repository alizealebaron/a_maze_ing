# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  output.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 15:31:24 by tcolson         #+#    #+#               #
#  Updated: 2026/02/21 17:08:07 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from src.maze.maze import Maze, Cell
from typing import Tuple


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def put_maze_val(maze: Maze, filename: str, path: str) -> None:
    """
    Writes the maze's structure and solution path to a file in a specific
    format. The maze is represented as a grid of hexadecimal values, where
    each value encodes the presence of walls around a cell. The function also
    includes the entry and exit coordinates, as well as the solution path.

    Args:
        maze (Maze): The maze object containing the grid and cell manipulation
        methods.
        filename (str): The name of the file to which the maze data will be
        written.
        path (str): A string representing the solution path through the maze,
                    typically consisting of characters like 'N', 'S', 'E', 'W'
                    for directions.
    """

    with open(filename, "w") as file:
        for y in range(1, maze.height - 1, 2):
            for x in range(1, maze.width - 1, 2):
                file.write(get_hex_val(maze, (x, y)))
            file.write("\n")
        file.write("\n")
        xentry, yentry = maze.entry
        file.write(f"{xentry},{yentry}\n")
        xexit, yexit = maze.exit
        file.write(f"{xexit},{yexit}\n")
        file.write(f"{path}\n")


def get_hex_val(maze: Maze, cell: Tuple[int, int]) -> str:
    """
    Converts the presence of walls around a given cell in the maze into a
    hexadecimal value. The function checks the four cardinal directions (North,
    East, South, West) for walls and assigns a specific value to each
    direction:
    - North: 1
    - East: 2
    - South: 4
    - West: 8

    The resulting hexadecimal value is a combination of these values based on
    the presence of walls around the cell. For example, if there are walls to
    the North and East, the value would be 3 (1 for North + 2 for East), which
    is represented as '3' in hexadecimal. If there are walls in all four
    directions, the value would be 15 (1 + 2 + 4 + 8), which is 'F' in
    hexadecimal.

    Args:
        maze (Maze): The maze object containing the grid and cell manipulation
        methods.
        cell (Tuple[int, int]): A tuple representing the (x, y) coordinates of
                                the cell for which to calculate the hexadecimal
                                value.

    Returns:
        str: A single hexadecimal character representing the presence of walls
             around the cell.
    """

    x, y = cell
    val = 0
    if y == 0 or maze.maze[(x, y - 1)] in [Cell.WALL, Cell.STRICT]:
        val += 1
    if x == maze.width or maze.maze[(x + 1, y)] in [Cell.WALL, Cell.STRICT]:
        val += 2
    if y == maze.height or maze.maze[(x, y + 1)] in [Cell.WALL, Cell.STRICT]:
        val += 4
    if x == 0 or maze.maze[(x - 1, y)] in [Cell.WALL, Cell.STRICT]:
        val += 8
    return hex(val).strip("0x").capitalize()
