from enum import Enum
from typing import Tuple


class Cell(Enum):
    ENTRY = "E"
    EXIT = "X"
    Blank = " "
    WALL = "#"
    STRICT = "*"
    SOLVE = "v"


class MazeError(Exception):
    pass


class Maze:
    def __init__(self, width: int, height: int,
                 entry: Tuple[int, int], exit: Tuple[int, int]) -> None:
        self.width: int = width
        self.height: int = height
        self.entry: tuple = entry
        self.exit: tuple = exit
        self.maze: dict = {}
        for x in range(width):
            for y in range(height):
                if (x == 0 or y == 0 or x == width - 1 or y == height - 1):
                    self.maze.update({(x, y): Cell.STRICT})
                else:
                    self.maze.update({(x, y): Cell.WALL})
        self.maze[entry] = Cell.ENTRY
        self.maze[exit] = Cell.EXIT

    def show_maze(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                print(f"{self.maze[(x, y)].value}", end="")
            print()

    def change_cell(self, cell: Tuple[int, int], val: Cell) -> None:
        if cell in [self.entry, self.exit] or self.maze[cell] == Cell.STRICT:
            raise MazeError("This cell can't be edited")
        if not isinstance(val, Cell):
            raise MazeError("Invalid value, should be of Cell type")
        self.maze[cell] = val


m = Maze(10, 15, (1, 1), (5, 5))
try:
    m.change_cell((5, 8), Cell.Blank)
    m.show_maze()
except Exception as e:
    print(e)