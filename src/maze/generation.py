# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  generation.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 15:33:35 by alebaron        #+#    #+#               #
#  Updated: 2026/02/12 17:12:18 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from .maze import Maze, Cell, MazeError
from random import randint
import random


# +-------------------------------------------------------------------------+
# |                              Side Winder                                |
# +-------------------------------------------------------------------------+

def side_winder(maze: Maze) -> None:
    for x in range(maze.width):
        try:
            maze.change_cell((x, maze.height - 1), Cell.BLANK)
        except MazeError:
            pass
    for y in range(0, maze.height, 2):
        xvalmax = randint(2, int(maze.width/3))
        xdoor = True
        for x in range(maze.width - 1):
            try:
                if x == xvalmax:
                    x += 1
                    xvalmax = x + randint(2, int(maze.width/3))
                    if xdoor and not y == 0:
                        maze.change_cell((x, maze.height - y), Cell.BLANK)
                    xdoor = True
                else:
                    maze.change_cell((x, maze.height - y - 1), Cell.BLANK)
                    if xdoor:
                        door = bool(randint(0, 1))
                        if door and not y == 0:
                            if not maze.maze[(x, maze.height - y)] in [Cell.WALL, Cell.STRICT]:
                                maze.change_cell((x, maze.height - y), Cell.BLANK)
                                xdoor = False
            except MazeError:
                x += 1
                xvalmax = x + randint(1, int(maze.width/3))


def new(maze: Maze) -> None:
    for y in range(0, maze.height, 2):
        for x in range(0, maze.width, 2):
            try:
                maze.change_cell((x, y), Cell.BLANK)
            except MazeError:
                pass

    for y in range(0, maze.height, 2):
        xvalmax = randint(0, int(maze.width/3))
        for x in range(1, maze.width, 2):
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

def get_unvisited_neibourg(maze: Maze, coord: tuple, visited: list,
                           config: dict) -> list:

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


def hunt_and_kill(maze: Maze, config: dict) -> None:

    # Get the seed
    if config["SEED"]:
        random.seed(config["SEED"])

    # Initialization of visited cells

    visited_cell = []

    # Initialization of list of direction

    lst_direction = ["N", "S", "E", "O"]

    # Begin of hunt

    cell = config["ENTRY"]
    visited_cell.append(cell)

    un_neibourg = get_unvisited_neibourg(maze, cell, visited_cell, config)

    while (len(un_neibourg) > 0):

        x, y = cell

        # Randomize a direction
        direction = random.choice(un_neibourg)

        un_neibourg = get_unvisited_neibourg(maze, direction, visited_cell,
                                             config)

        if (maze.is_editable(direction)):
            maze.change_cell(direction, Cell.BLANK)

        visited_cell.append(direction)
        print(f"visited_cell : {visited_cell}")
        print(f"un_neibourg : {un_neibourg}")
