# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  theme.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 11:39:36 by tcolson         #+#    #+#               #
#  Updated: 2026/02/20 11:51:24 by tcolson         ###   ########.fr        #
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
             "SOLVE": Color.GREEN}

    PACMAN = {"STRICT": Color.BLUE,
              "WALL": Color.SKY_BLUE,
              "BLANK": Color.BLACK,
              "ENTRY": Color.GOLD,
              "EXIT": Color.WHITE,
              "SOLVE": Color.WHITE}

    MOTHERBOARD = {"STRICT": Color.GREEN,
                   "WALL": Color.GOLD,
                   "BLANK": Color.LIGHT_GRAY,
                   "ENTRY": Color.GOLD,
                   "EXIT": Color.RED,
                   "SOLVE": Color.GOLD}

    def __str__(self):
        return self.value
