# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 15:31:04 by tcolson         #+#    #+#               #
#  Updated: 2026/02/13 12:47:06 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from enum import Enum
from typing import Tuple, Dict


class Color(Enum):
    RESET = "\033[0m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    LIGHT_GRAY = "\033[37m"

    DARK_GRAY = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    GOLD = "\033[93m"
    SKY_BLUE = "\033[94m"
    PINK = "\033[95m"
    TURQUOISE = "\033[96m"
    WHITE = "\033[97m"

    ORANGE = "\033[38;5;208m"
    CORAL = "\033[38;5;203m"
    LIME = "\033[38;5;118m"
    BROWN = "\033[38;5;130m"

    def __str__(self):
        return self.value


class Cell(Enum):
    ENTRY = "E"
    EXIT = "X"
    BLANK = "░"
    WALL = "█"
    STRICT = "▒"
    SOLVE = "8"


class MazeError(Exception):
    pass


class Maze:
    def __init__(self, width: int, height: int,
                 entry: Tuple[int, int], exit: Tuple[int, int],
                 color: Dict[str, Color]) -> None:
        self.width: int = width
        self.height: int = height
        self.entry: tuple = (-1, -1)
        self.exit: tuple = (-1, -1)
        self.maze: dict = {}
        self.color: dict = color
        for x in range(width):
            for y in range(height):
                self.maze.update({(x, y): Cell.WALL})
        self.put_logo()
        try:
            self.change_cell(entry, Cell.ENTRY)
            self.entry = entry
        except MazeError:
            print("Error: can't place entry")
        try:
            self.change_cell(exit, Cell.EXIT)
            self.exit = exit
        except MazeError:
            print("Error: can't place exit")

    def change_cell(self, cell: Tuple[int, int], val: Cell) -> None:
        x, y = cell
        if x > self.width or y > self.height:
            raise MazeError("Cell is not even in the maze")
        if cell in [self.entry, self.exit] or self.maze[cell] == Cell.STRICT:
            raise MazeError(f"This cell can't be edited, {cell}")
        if not isinstance(val, Cell):
            raise MazeError("Invalid value, should be of Cell type")
        self.maze[cell] = val

    def is_editable(self, cell: Tuple[int, int]) -> bool:
        x, y = cell
        if x > self.width or y > self.height:
            return False
        if cell in [self.entry, self.exit] or self.maze[cell] == Cell.STRICT:
            return False

        return True


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

        else:
            print(f"{MazeError().__class__.__name__}: Can't draw 42 pattern.")

    def show_maze(self) -> None:
        # Top border
        for x in range(self.width + 2):
            print(f"{self.color['STRICT']}{Cell.STRICT.value}", end="")
        print()
        # Maze
        for y in range(self.height):
            print(f"{self.color['STRICT']}{Cell.STRICT.value}", end="")
            for x in range(self.width):
                print(f"{self.color[self.maze[(x, y)].name]}", end="")
                print(f"{self.maze[(x, y)].value}", end="")
            print(f"{self.color['STRICT']}{Cell.STRICT.value}")
        # Lower border
        for x in range(self.width + 2):
            print(f"{self.color['STRICT']}{Cell.STRICT.value}", end="")
        print(Color.RESET.value)
