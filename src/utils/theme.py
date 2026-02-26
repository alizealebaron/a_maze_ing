# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  theme.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 11:39:36 by tcolson         #+#    #+#               #
#  Updated: 2026/02/24 11:56:28 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from enum import Enum
from src.maze.Maze import Color


# +-------------------------------------------------------------------------+
# |                                  Enum                                   |
# +-------------------------------------------------------------------------+

class Theme(Enum):
    """
    An enumeration of themes that can be applied to the maze.
    """

    BULBASAUR = {"STRICT": Color.TURQUOISE,
                 "WALL": Color.GREEN,
                 "BLANK": Color.PINK,
                 "ENTRY": Color.CORAL,
                 "EXIT": Color.LIME,
                 "SOLVE": Color.CYAN}

    RETRO = {"STRICT": Color.GREEN,
             "WALL": Color.ORANGE,
             "BLANK": Color.SKY_BLUE,
             "ENTRY": Color.RED,
             "EXIT": Color.WHITE,
             "SOLVE": Color.GREEN}

    PACMAN = {"STRICT": Color.BLUE,
              "WALL": Color.SKY_BLUE,
              "BLANK": Color.BLACK,
              "ENTRY": Color.GOLD,
              "EXIT": Color.WHITE,
              "SOLVE": Color.WHITE}

    LAKERS = {"STRICT": Color.PINK,
              "WALL": Color.YELLOW,
              "BLANK": Color.GOLD,
              "ENTRY": Color.WHITE,
              "EXIT": Color.RED,
              "SOLVE": Color.WHITE}

    INVISIBLE = {"STRICT": Color.BLACK,
                 "WALL": Color.BLACK,
                 "BLANK": Color.BLACK,
                 "ENTRY": Color.BLACK,
                 "EXIT": Color.BLACK,
                 "SOLVE": Color.WHITE}

    EVIL = {"STRICT": Color.RED,
            "WALL": Color.RED,
            "BLANK": Color.BLACK,
            "ENTRY": Color.RED,
            "EXIT": Color.RED,
            "SOLVE": Color.RED}

    BLACKNWHITE = {"STRICT": Color.WHITE,
                   "WALL": Color.WHITE,
                   "BLANK": Color.BLACK,
                   "ENTRY": Color.WHITE,
                   "EXIT": Color.WHITE,
                   "SOLVE": Color.WHITE}

    def __str__(self) -> str:
        return str(self.value)
