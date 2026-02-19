# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  theme.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 11:39:36 by tcolson         #+#    #+#               #
#  Updated: 2026/02/16 14:13:06 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from enum import Enum
from src.maze.maze import Color


# +-------------------------------------------------------------------------+
# |                                  Enum                                   |
# +-------------------------------------------------------------------------+

class Theme(Enum):
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
             "SOLVE": Color.CYAN}

    PACMAN = {"STRICT": Color.BLUE,
              "WALL": Color.SKY_BLUE,
              "BLANK": Color.BLACK,
              "ENTRY": Color.GOLD,
              "EXIT": Color.WHITE,
              "SOLVE": Color.CYAN}

    MOTHERBOARD = {"STRICT": Color.WHITE,
                   "WALL": Color.BLACK,
                   "BLANK": Color.LIME,
                   "ENTRY": Color.GOLD,
                   "EXIT": Color.RED,
                   "SOLVE": Color.CYAN}

    def __str__(self):
        return self.value
