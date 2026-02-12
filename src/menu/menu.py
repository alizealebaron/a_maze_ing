# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  menu.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:09:51 by alebaron        #+#    #+#               #
#  Updated: 2026/02/12 13:03:22 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from src.utils.color import Color


# +-------------------------------------------------------------------------+
# |                            Input Functions                              |
# +-------------------------------------------------------------------------+

def regen_maze():
    # TODO
    print("You choose to regen the maze")


def show_hide_path():
    # TODO
    print("You choose to show or hide the path")


def show_hide_graphic():
    # TODO
    print("You choose to show or hide the graphic maze")


def rotate_maze_color():
    # TODO
    print("You choose to rotate maze color")


def end_program():
    print("End of the program, bye !")
    exit(2)


# +-------------------------------------------------------------------------+
# |                                Variable                                 |
# +-------------------------------------------------------------------------+

dict_menu_data = {
    1: {
        "name": "Re-generate a new maze",
        "color": Color.SKY_BLUE,
        "function": regen_maze,
    },
    2: {
        "name": "Show/Hide path from entry to exit",
        "color": Color.GREEN,
        "function": show_hide_path,
    },
    3: {
        "name": "Show/Hide graphic maze",
        "color": Color.GOLD,
        "function": show_hide_graphic,
    },
    4: {
        "name": "Rotate maze colors",
        "color": Color.PINK,
        "function": rotate_maze_color,
    },
    5: {
        "name": "Quit",
        "color": Color.RED,
        "function": end_program,
    }
}


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def manage_user_input(user_input: int) -> None:
    dict_menu_data[int(user_input)]["function"]()


def print_menu() -> None:

    def get_title() -> str:
        return (f"{Color.ORANGE}{Color.BOLD}A_maze_ing menu{Color.RESET}")

    def print_option() -> str:
        for key, value in dict_menu_data.items():
            str_temp = f"{value['color']}{key}. {value['name']}{Color.RESET}"
            print(f"║ {str_temp:70}║")

    print("")
    print("╔══════════════════════════════════════════════════════════════╗")
    print(f"║                       {get_title()}                        ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                                                              ║")
    print_option()
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("")
