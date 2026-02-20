# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  menu.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:09:51 by alebaron        #+#    #+#               #
#  Updated: 2026/02/20 14:45:40 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from src.maze.maze import Color, Maze
from src.utils.effect import Effect
from src.utils.theme import Theme
from typing import Dict
from random import choice, seed
from src.maze.generation import hunt_and_kill
from src.maze.resolution import resolution
from src.utils.error import MenuError, print_error


# +-------------------------------------------------------------------------+
# |                            Input Functions                              |
# +-------------------------------------------------------------------------+

def regen_maze(maze: Maze, config: dict, color: dict):

    maze.clean_maze()
    hunt_and_kill(maze, config)
    resolution(maze, config)
    return maze


def show_hide_path(maze: Maze, config: dict):
    print("\nYou choose to show or hide the path\n")

    def clean():
        maze.clean_path()
        print(maze.show_maze())

    def show():
        path = resolution(maze, config)
        print(f"The exit is {len(path)} steps away from the entry!")

    if config["HIDE"]:
        config["HIDE"] = not config["HIDE"]
        show()
    else:
        clean()
        config["HIDE"] = not config["HIDE"]


def change_maze_settings(config: dict):

    def manage_user_input(user_input: int, config: dict):
        if user_input == 1:
            val = int(input("Enter the new Width: "))
            config["WIDTH"] = val
            val = int(input("Enter the new Height: "))
            config["HEIGHT"] = val
        elif user_input == 2:
            val = input("Enter the new Entry position: ")
        elif user_input == 3:
            val = input("Enter the new Exit position: ")
        elif user_input == 5:
            return

    while (True):
        try:
            print_menu(config)
            user_input = input("Pick what you want to change: ")
            if (user_input.isdigit() is False):
                print_error(MenuError(), "Bad Input, "
                            + "must be an integer (1-5)")
            elif int(user_input) == 5:
                break
            else:
                manage_user_input(int(user_input), config)
                print()

        except Exception as e:
            print(e)


def rotate_maze_color(maze: Maze, color: Dict[str, Color]) -> None:

    def get_title() -> str:
        return f"{Effect.BOLD}{Color.ORANGE}Theme Selector{Color.RESET}"

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
    print(maze.show_maze())


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
        "name": "Change maze settings",
        "color": Color.GOLD,
        "function": change_maze_settings,
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
        "name": "Laker",
        "color": Color.PINK,
        "theme": Theme.LAKERS
    },
    6: {
        "name": "Invisible",
        "color": Color.LIGHT_GRAY,
        "theme": Theme.INVISIBLE
    },
    7: {
        "name": "Evil",
        "color": Color.RED,
        "theme": Theme.EVIL
    },
    8: {
        "name": "Black and White",
        "color": Color.WHITE,
        "theme": Theme.BLACKNWHITE
    }
}


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def manage_user_input(user_input: int, color: Dict[str, Color],
                      maze: Maze, config: dict) -> None:
    if int(user_input) == 1:
        dict_menu_data[int(user_input)]["function"](maze, config, color)
    elif int(user_input) == 2:
        dict_menu_data[int(user_input)]["function"](maze, config)
    elif int(user_input) == 3:
        dict_menu_data[int(user_input)]["function"](config)
    elif int(user_input) == 4:
        dict_menu_data[int(user_input)]["function"](maze, color)
    else:
        dict_menu_data[int(user_input)]["function"]()


def print_menu(config: dict) -> None:

    def get_title() -> str:
        return (f"{Color.ORANGE}{Effect.BOLD}A_maze_ing menu{Color.RESET}")

    def print_option() -> None:
        for key, value in dict_menu_data.items():
            str_temp = f"{value['color']}{key}. {value['name']}{Color.RESET}"
            print(f"║ {str_temp:70}║")

    print("")
    print_seed(config)
    print("╔══════════════════════════════════════════════════════════════╗")
    print(f"║                       {get_title()}                        ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print("║                                                              ║")
    print_option()
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("")


def print_seed(config: dict) -> None:

    try:
        seed = config["SEED"]
    except Exception:
        seed = config["RANDOM_SEED"]

    print(f"Seed : {seed}")


def get_random_color(color: Dict[str, Color]) -> None:
    seed()
    color_list = list(Color)
    color["STRICT"] = choice(color_list).value
    color["WALL"] = choice(color_list).value
    color["BLANK"] = choice(color_list).value
    color["SOLVE"] = choice(color_list).value
    if color["BLANK"] in [color["WALL"], color["STRICT"], color["SOLVE"]]:
        get_random_color(color)
        return
    bg = color["BLANK"]
    bgval = bg[color["BLANK"].index("[")+1]
    bgend = bg[color["BLANK"].index("[")+2:len(bg)]
    bg = "\033[" + str(int(bgval) + 1) + bgend
    color["BLANK"] = bg
    color["SOLVE"] += bg
    color["ENTRY"] = choice(color_list).value + bg
    color["EXIT"] = choice(color_list).value + bg


def init_color() -> Dict[str, Color]:
    color = {"STRICT": Color.WHITE,
             "WALL": Color.WHITE,
             "ENTRY": Color.LIME,
             "EXIT": Color.RED,
             "BLANK": Color.BLACK,
             "SOLVE": Color.GOLD}
    return color


def set_theme(color: Dict[str, Color], theme: Theme):
    color["STRICT"] = theme.value["STRICT"]
    color["WALL"] = theme.value["WALL"]
    color["BLANK"] = theme.value["BLANK"]
    bg = color["BLANK"].value
    bgval = bg[color["BLANK"].value.index("[")+1]
    bgend = bg[color["BLANK"].value.index("[")+2:len(bg)]
    bg = "\033[" + str(int(bgval) + 1) + bgend
    color["BLANK"] = bg
    color["SOLVE"] = theme.value["SOLVE"].value + bg
    color["ENTRY"] = theme.value["ENTRY"].value + bg
    color["EXIT"] = theme.value["EXIT"].value + bg
