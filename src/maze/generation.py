from src.maze.maze import Maze, Cell, MazeError
from random import randint


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
