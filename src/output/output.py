# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  output.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 15:31:24 by tcolson         #+#    #+#               #
#  Updated: 2026/02/17 10:51:33 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from src.maze.maze import Maze, Cell
from typing import Tuple


def put_maze_val(maze: Maze, filename: str, path: str) -> None:
    with open(filename, "w") as file:
        for y in range(maze.height - 1):
            for x in range(maze.width - 1):
                file.write(get_hex_val(maze, (x, y)))
            file.write("\n")
        file.write("\n")
        xentry, yentry = maze.entry
        file.write(f"{xentry}, {yentry}\n")
        xexit, yexit = maze.exit
        file.write(f"{xexit}, {yexit}\n")
        file.write(f"{path}\n")


def get_hex_val(maze: Maze, cell: Tuple[int, int]) -> str:
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
