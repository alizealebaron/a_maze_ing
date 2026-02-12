from src.maze.maze import Maze, Cell, MazeError
from random import randint


def side_winder(maze: Maze) -> None:
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
