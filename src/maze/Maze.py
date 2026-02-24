# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 15:31:04 by tcolson         #+#    #+#               #
#  Updated: 2026/02/24 11:19:11 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from enum import Enum
from typing import Tuple, Dict
import sys


# +-------------------------------------------------------------------------+
# |                                   Enum                                  |
# +-------------------------------------------------------------------------+

class Color(Enum):
    """
    An enumeration of ANSI escape sequences for terminal text coloring.

    This class provides a set of color constants that can be used to format
    terminal output. It includes standard colors, bright variants, and specific
    256-color palette codes.
    """

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    LIGHT_GRAY = "\033[37m"
    BLACK = "\033[30m"

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

    RESET = "\033[0m"

    def __str__(self) -> str:
        """
        Returns the ANSI escape sequence string associated with the color.

        Returns:
            str: The raw ANSI color code.
        """
        return self.value


class Cell(Enum):
    """
    An enumeration representing different types of cells in a
    maze or grid system.

    Attributes:
        ENTRY (str): Represents the starting point ("E").
        EXIT (str): Represents the destination point ("X").
        BLANK (str): Represents an empty, navigable path (" ").
        WALL (str): Represents a solid, impassable barrier ("█").
        STRICT (str): Represents a restricted or special movement area ("▒").
        SOLVE (str): Represents a point belonging to the calculated
        solution path ("•").
    """
    ENTRY = "E"
    EXIT = "X"
    BLANK = " "
    WALL = "█"
    STRICT = "▒"
    SOLVE = "•"


# +-------------------------------------------------------------------------+
# |                                 Class                                   |
# +-------------------------------------------------------------------------+

class MazeError(Exception):
    """
    Custom exception class for handling errors related
    to maze operations.
    """
    pass


class Maze:
    """
    A class representing a maze structure with customizable+
    themes and cell types.

    Attributes:
        width (int): The width of the maze.
        height (int): The height of the maze.
        entry (Tuple[int, int]): The coordinates of the maze entry point.
        exit (Tuple[int, int]): The coordinates of the maze exit point.
        maze (Dict[Tuple[int, int], Cell]): A dictionary mapping
            cell coordinates to their types.
        color (Dict[str, Color]): A dictionary mapping cell types
            to their corresponding colors.
        THEMES (Dict[str, Dict[str, str]]): A dictionary of themes
            for visual representation of the maze.
        key (Dict[str, str]): The current theme's mapping of
            cell types to their visual representations.

    Methods:
        __init__(self, width: int, height: int, entry: Tuple[int, int],
        exit: Tuple[int, int], color: Dict[str, Color]) -> None:
            Initializes the maze with the specified dimensions,
            entry and exit points, and color scheme.

        change_cell(self, cell: Tuple[int, int], val: Cell) -> None:
            Changes the type of a specific cell in the maze,
            ensuring it is editable and valid.

        is_editable(self, cell: Tuple[int, int]) -> bool:
            Checks if a specific cell can be edited
            (i.e., it is not an entry, exit, or strict cell).

        is_ok_for_logo(self) -> bool:
            Determines if the maze dimensions are sufficient
            to accommodate a predefined logo pattern.

        put_logo(self) -> None:
            Places a predefined logo pattern in the center
            of the maze if the dimensions allow for it.

        clean_maze(self) -> None:
            Resets all editable cells in the maze to be walls.

        clean_path(self) -> None:
            Resets all cells marked as part of the solution path back to blank.

        show_maze(self) -> str:
            Generates a string representation of the maze,
            including borders and colored cell types.

        change_keys(self, key: int | str) -> None:
            Changes the current theme for visual representation
            of the maze based on a provided key.
    """

    def __init__(self, width: int, height: int,
                 entry: Tuple[int, int], exit: Tuple[int, int],
                 color: Dict[str, Color | str]) -> None:
        self.width: int = width
        self.height: int = height
        self.entry: tuple[int, int] = (-1, -1)
        self.exit: tuple[int, int] = (-1, -1)
        self.maze: dict[tuple[int, int], Cell] = {}
        self.color: dict[str, Color | str] = color

        for x in range(width):
            for y in range(height):
                self.maze.update({(x, y): Cell.WALL})
        self.put_logo()
        try:
            self.change_cell(entry, Cell.ENTRY)
            self.entry = entry
        except MazeError:
            print("Error: can't place entry")
            sys.exit(2)
        try:
            self.change_cell(exit, Cell.EXIT)
            self.exit = exit
        except MazeError:
            print("Error: can't place exit")
            sys.exit(2)

        self.THEMES = {
            "Default": {
                "ENTRY": "E", "EXIT": "X", "BLANK": " ",
                "WALL": "█", "STRICT": "▒", "SOLVE": "•"
            },
            "Cubic": {
                "ENTRY": "🟦", "EXIT": "🟥", "BLANK": "  ",
                "WALL": "⬛", "STRICT": "⬜", "SOLVE": "🟩"
            },
            "Emojis": {
                "ENTRY": "🚪", "EXIT": "🏁", "BLANK": "  ",
                "WALL": "🧱", "STRICT": "🚫", "SOLVE": "⭐"
            },
            "Animal": {
                "ENTRY": "🦭", "EXIT": "🦕", "BLANK": "  ",
                "WALL": "🦖", "STRICT": "🦆", "SOLVE": "🐢"
            }
        }

        self.key = self.THEMES["Default"]

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

    # Check if the size can handle the 42 logo

    def is_ok_for_logo(self) -> bool:
        if self.width < 9 or self.height < 7:
            return False
        else:
            return True

    # Print the logo in the middle of the maze

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

    def clean_maze(self) -> None:

        for x in range(0, self.width):
            for y in range(0, self.height):
                if (self.is_editable((x, y))):
                    self.change_cell((x, y), Cell.WALL)

    def clean_path(self) -> None:
        for x in range(0, self.width):
            for y in range(0, self.height):
                if (self.maze[(x, y)] == Cell.SOLVE):
                    self.change_cell((x, y), Cell.BLANK)

    def show_maze(self) -> str:
        str_maze = ""

        # Top border
        for x in range(self.width + 2):
            str_maze += (f"{self.color['STRICT']}{self.key['STRICT']}")
        str_maze += "\n"
        # Maze
        for y in range(self.height):
            str_maze += (f"{self.color['STRICT']}{self.key['STRICT']}")
            for x in range(self.width):
                str_maze += f"{self.color[self.maze[(x, y)].name]}"
                str_maze += f"{self.key[self.maze[(x, y)].name]}"
                str_maze += Color.RESET.value
            str_maze += f"{self.color['STRICT']}{self.key['STRICT']}\n"
        # Lower border
        for x in range(self.width + 2):
            str_maze += f"{self.color['STRICT']}{self.key['STRICT']}"
        str_maze += Color.RESET.value

        return str_maze

    def change_keys(self, key: str) -> None:

        try:
            self.key = self.THEMES[key]
        except KeyError:
            print(f"{MazeError().__class__.__name__}: "
                  "Wrong key in change_keys()")
