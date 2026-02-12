# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  menu.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:09:51 by alebaron        #+#    #+#               #
#  Updated: 2026/02/12 12:05:53 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+

from src.utils.color import Color

# +-------------------------------------------------------------------------+
# |                                Variable                                 |
# +-------------------------------------------------------------------------+


dict_menu_data = {
    "Re-generate a new maze": Color.SKY_BLUE,
    "Show/Hide path from entry to exit": Color.GREEN,
    "Show/Hide graphic maze": Color.GOLD,
    "Rotate maze colors": Color.PINK,
    "Quit": Color.RED,
}


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+


def print_menu() -> None:

    def get_title() -> str:
        return (f"{Color.ORANGE}{Color.BOLD}A_maze_ing menu{Color.RESET}")

    def print_option() -> str:
        i = 1
        for key in dict_menu_data:
            str_temp = f"{dict_menu_data[key]}{i}. {key}{Color.RESET}"
            print(f"║ {str_temp:70}║")
            i += 1

    print(f"╔══════════════════════════════════════════════════════════════╗")
    print(f"║                       {get_title()}                        ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║                                                              ║")
    print_option()
    print(f"║                                                              ║")
    print(f"╚══════════════════════════════════════════════════════════════╝")

