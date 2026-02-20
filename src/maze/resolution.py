# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  resolution.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 12:39:18 by tcolson         #+#    #+#               #
#  Updated: 2026/02/19 16:28:09 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .maze import Maze, Cell
from rich.live import Live
from rich.text import Text
from time import sleep


def resolution(maze: Maze, config: dict) -> str:
    """Search the shortest path, draw it and return it"""

    width = config["WIDTH"]
    height = config["HEIGHT"]
    path = ""

    def explore_cell(cell: tuple[int, int], live: Live):
        maze.change_cell(cell, Cell.SOLVE)
        live.update(Text.from_ansi(maze.show_maze()))
        sleep(0.05)

    def get_directions(pos: tuple) -> list[tuple]:
        """Give the directions in most efficient order"""
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

    def solve(pos: tuple, live: Live) -> bool:
        """Look recursively for the shortest path"""
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

    with Live("", refresh_per_second=25) as live:

        solve(config["ENTRY"], live)

        maze_render = Text.from_ansi(maze.show_maze())
        live.update(maze_render)
    return path[::-1]
