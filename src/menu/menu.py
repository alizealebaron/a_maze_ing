# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  menu.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:09:51 by alebaron        #+#    #+#               #
#  Updated: 2026/02/16 12:33:35 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from src.maze.maze import Color, Maze
from src.utils.effect import Effect
from src.utils.theme import Theme
from typing import Dict
from random import choice
from src.maze.generation import hunt_and_kill


# +-------------------------------------------------------------------------+
# |                            Input Functions                              |
# +-------------------------------------------------------------------------+

def regen_maze(maze: Maze, config: dict):
    hunt_and_kill(maze, config)


def show_hide_path():
    # TODO
    print("You choose to show or hide the path")


def show_hide_graphic():
    # TODO
    print("You choose to show or hide the graphic maze")


def rotate_maze_color(color: Dict[str, Color]) -> None:

    def get_title() -> str:
        return f"{Color.ORANGE}Theme Selector{Color.RESET}"

    def print_option() -> None:
        for key, value in dict_theme_data.items():
            str_temp = f"{value['color']}{key}. {value['name']}{Color.RESET}"
            print(f"║ {str_temp:70}║")

    print("You choose to rotate maze color")
    print("")
    print("╔══════════════════════════════════════════════════════════════╗")
    print(f"║                       {get_title()}                         ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                                                              ║")
    print_option()
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("")
    user_choice = input("Pick the theme that you want: ")
    if int(user_choice) == 1:
        get_random_color(color)
    else:
        set_theme(color, dict_theme_data[int(user_choice)]["theme"])


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

dict_theme_data = {
    1: {
        "name": "Random theme generator",
        "color": Color.SKY_BLUE,
        "theme": None
    },
    2: {
        "name": "Bulbasaur",
        "color": Color.TURQUOISE,
        "theme": Theme.BULBASAUR
    },
    3: {
        "name": "Retro",
        "color": Color.GREEN,
        "theme": Theme.RETRO
    },
    4: {
        "name": "Pac-MAN",
        "color": Color.GOLD,
        "theme": Theme.PACMAN
    },
    5: {
        "name": "Motherboard",
        "color": Color.LIGHT_GRAY,
        "theme": Theme.MOTHERBOARD
    }
}


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def manage_user_input(user_input: int, color: Dict[str, Color], config: dict) -> None:
    if int(user_input) == 1:
        dict_menu_data[int(user_input)]["function"](config)
    if int(user_input) == 4:
        dict_menu_data[int(user_input)]["function"](color)
    else:
        dict_menu_data[int(user_input)]["function"]()


def print_menu() -> None:

    def get_title() -> str:
        return (f"{Color.ORANGE}{Effect.BOLD}A_maze_ing menu{Color.RESET}")

    def print_option() -> None:
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


def get_random_color(color: Dict[str, Color]) -> None:
    color_list = list(Color)
    color["STRICT"] = choice(color_list)
    color["WALL"] = choice(color_list)
    color["ENTRY"] = choice(color_list)
    color["EXIT"] = choice(color_list)
    color["BLANK"] = choice(color_list)


def init_color() -> Dict[str, Color]:
    color = {"STRICT": Color.WHITE,
             "WALL": Color.WHITE,
             "ENTRY": Color.LIME,
             "EXIT": Color.RED,
             "BLANK": Color.BLACK}
    return color


def set_theme(color: Dict[str, Color], theme: Theme):
    color["STRICT"] = theme.value["STRICT"]
    color["WALL"] = theme.value["WALL"]
    color["ENTRY"] = theme.value["ENTRY"]
    color["EXIT"] = theme.value["EXIT"]
    color["BLANK"] = theme.value["BLANK"]
