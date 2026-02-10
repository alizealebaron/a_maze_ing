from enum import Enum
from typing import Tuple
from random import randint


class Cell(Enum):
    ENTRY = "E"
    EXIT = "X"
    BLANK = " "
    WALL = "█"
    STRICT = "░"
    SOLVE = "*"


class MazeError(Exception):
    pass


class Maze:
    def __init__(self, width: int, height: int,
                 entry: Tuple[int, int], exit: Tuple[int, int]) -> None:
        self.width: int = width
        self.height: int = height
        self.entry: tuple = (-1, -1)
        self.exit: tuple = (-1, -1)
        self.maze: dict = {}
        for x in range(width):
            for y in range(height):
                # if (x == 0 or y == 0 or x == width - 1 or y == height - 1):
                #     self.maze.update({(x, y): Cell.STRICT})
                # else:
                self.maze.update({(x, y): Cell.WALL})
        self.put_logo()
        try:
            self.change_cell(entry, Cell.ENTRY)
        except MazeError:
            print("Error: can't place entry")
        try:
            self.change_cell(exit, Cell.EXIT)
        except MazeError:
            print("Error: can't place exit")

    def change_cell(self, cell: Tuple[int, int], val: Cell) -> None:
        if cell in [self.entry, self.exit] or self.maze[cell] == Cell.STRICT:
            raise MazeError(f"This cell can't be edited, {cell}")
        if not isinstance(val, Cell):
            raise MazeError("Invalid value, should be of Cell type")
        self.maze[cell] = val

    def is_ok_for_logo(self) -> bool:
        if self.width < 9 or self.height < 7:
            return False
        else:
            return True

    def put_logo(self) -> None:
        if self.is_ok_for_logo():
            midx, midy = (int(self.width/2), int(self.height/2))
            # ## 4 ## #
            self.change_cell((midx - 1, midy), Cell.STRICT)
            self.change_cell((midx - 2, midy), Cell.STRICT)
            self.change_cell((midx - 3, midy), Cell.STRICT)
            self.change_cell((midx - 3, midy - 1), Cell.STRICT)
            self.change_cell((midx - 3, midy - 2), Cell.STRICT)
            self.change_cell((midx - 1, midy + 1), Cell.STRICT)
            self.change_cell((midx - 1, midy + 2), Cell.STRICT)

            # ## 2 ## #
            self.change_cell((midx + 1, midy), Cell.STRICT)
            self.change_cell((midx + 2, midy), Cell.STRICT)
            self.change_cell((midx + 3, midy), Cell.STRICT)
            self.change_cell((midx + 3, midy - 1), Cell.STRICT)
            self.change_cell((midx + 3, midy - 2), Cell.STRICT)
            self.change_cell((midx + 1, midy - 2), Cell.STRICT)
            self.change_cell((midx + 2, midy - 2), Cell.STRICT)
            self.change_cell((midx + 1, midy + 1), Cell.STRICT)
            self.change_cell((midx + 1, midy + 2), Cell.STRICT)
            self.change_cell((midx + 2, midy + 2), Cell.STRICT)
            self.change_cell((midx + 3, midy + 2), Cell.STRICT)

    def show_maze(self) -> None:
        for x in range(self.width + 2):
            print(Cell.STRICT.value, end="")
        print()
        for y in range(self.height):
            print(Cell.STRICT.value, end="")
            for x in range(self.width):
                print(f"{self.maze[(x, y)].value}", end="")
            print(Cell.STRICT.value)
        for x in range(self.width + 2):
            print(Cell.STRICT.value, end="")
        print()


m = Maze(9, 7, (0, 0), (5, 2))
try:
    # m.change_cell((2, 1), Cell.BLANK)
    # m.change_cell((3, 1), Cell.BLANK)
    m.show_maze()
except Exception as e:
    print(e)