# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  resolution.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 12:39:18 by tcolson         #+#    #+#               #
#  Updated: 2026/02/17 11:03:48 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .maze import Maze, Cell
from rich.live import Live
from rich.text import Text


def resolution(maze: Maze, config: dict) -> None:

    width = config["WIDTH"]
    height = config["HEIGHT"]
    path = ""

    def solve(pos: tuple) -> bool:
        x, y = pos
        directions = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        nonlocal path

        for nx, ny in directions:
            newpos = (nx, ny)

            if nx > width - 1 or nx < 0 or ny > height - 1 or ny < 0:
                pass
            else:
                if maze.maze[newpos] == Cell.EXIT:
                    if newpos == directions[0]:
                        path += "N"
                    if newpos == directions[1]:
                        path += "S"
                    if newpos == directions[2]:
                        path += "W"
                    if newpos == directions[3]:
                        path += "E"
                    return True
                elif maze.maze[newpos] == Cell.BLANK:
                    maze.change_cell(newpos, Cell.SOLVE)
                    res = solve(newpos)
                    if res:
                        if newpos == directions[0]:
                            path += "N"
                        if newpos == directions[1]:
                            path += "S"
                        if newpos == directions[2]:
                            path += "W"
                        if newpos == directions[3]:
                            path += "E"
                        return True
                    else:
                        maze.change_cell(newpos, Cell.BLANK)
        return False

    with Live("", refresh_per_second=25) as live:

        solve(config["ENTRY"])
        for cell in maze.maze.keys():
            maze_render = Text.from_ansi(maze.show_maze())
            live.update(maze_render)
    return path[::-1]
