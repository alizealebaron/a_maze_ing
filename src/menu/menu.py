# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  menu.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:09:51 by alebaron        #+#    #+#               #
#  Updated: 2026/02/23 14:59:38 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from src.maze.maze import Color, Maze
from src.utils.effect import Effect
from src.utils.theme import Theme
from typing import Dict, Callable, cast
from random import choice, seed
from src.maze.generation import hunt_and_kill
from src.maze.resolution import resolution
import os


# +-------------------------------------------------------------------------+
# |                            Input Functions                              |
# +-------------------------------------------------------------------------+

def regen_maze(maze: Maze, config: dict, color: dict) -> Maze:
    """
    Regenerate a new maze using the Hunt-and-Kill algorithm and solve it.
    This function first cleans the current maze, then generates a new maze
    using the Hunt-and-Kill algorithm.
    After the new maze is generated, itcalls the resolution function to find
    the path from the entry to the exit.
    Finally, it prints the newly generated maze.

    Args:
        maze (Maze): The maze object to be regenerated.
        config (dict): A configuration dictionary containing maze settings.
        color (dict): A dictionary containing color settings for the maze.
    """

    maze.clean_maze()
    hunt_and_kill(maze, config)
    if not config["HIDE"]:
        os.system("clear")
    path = resolution(maze, config)
    if not config["HIDE"]:
        print(f"The exit is {len(path)} steps away from the entry!")
    return maze


def show_hide_path(maze: Maze, config: dict) -> None:
    """
    Toggle the display of the path from the entry to the exit in the maze.
    This function checks the current state of the "HIDE" setting in the config.
    If "HIDE" is True, it will call the resolution function to find and display
    the path, and then set "HIDE" to False. If "HIDE" is False, it will clean
    the path from the maze and set "HIDE" to True.

    Args:
        maze (Maze): The maze object to be modified.
        config (dict): A configuration dictionary setting.
    """

    def clean() -> None:
        maze.clean_path()
        print(maze.show_maze())

    def show() -> None:
        path = resolution(maze, config)
        print(f"The exit is {len(path)} steps away from the entry!")

    if config["HIDE"]:
        config["HIDE"] = not config["HIDE"]
        show()
    else:
        clean()
        config["HIDE"] = not config["HIDE"]


def change_maze_settings(maze: Maze) -> None:
    """
    Change the ASCII characters used to represent different elements of the
    maze.
    This function displays a menu of available themes for the maze's ASCII
    representation. The user can select a theme by entering the corresponding
    number. The function then updates the maze's ASCII settings based on the
    selected theme and prints the updated maze.

    Args:
        maze (Maze): The maze object whose ASCII settings are to be changed.

    Method:
        get_title() -> str: Returns the title of the menu.
        print_option() -> None: Prints the available theme options for the
                                maze.

    """

    def get_title() -> str:
        return f"{Effect.BOLD}{Color.BRIGHT_RED}ASCII Selector{Color.RESET}"

    def print_option() -> None:
        i = 1
        color_list = list(Color)
        for key, _ in maze.THEMES.items():
            str_temp = f"{i}{color_list.pop(0).value}. {key}{Color.RESET}"
            print(f"║ {str_temp:70}║")
            i += 1

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
    try:
        maze.change_keys(list(maze.THEMES)[int(user_choice) - 1])
    except Exception:
        print(f"Error: Bad input, try a number between 1 and "
              f"{len(list(maze.THEMES))}")

    print(f"\n{maze.show_maze()}")


def rotate_maze_color(maze: Maze, color: Dict[str, Color | str]) -> None:
    """
    Rotate the colors used in the maze by shifting each color to
    the next one in the color dictionary. This function updates
    the color settings for the maze by rotating the colors in the
    color dictionary. It then prints the maze with the new color settings.

    Args:
        maze (Maze): The maze object whose colors are to be rotated.
        color (Dict[str, Color]): A dictionary containing the current color
                                settings for the maze.

    Method:
        get_title() -> str: Returns the title of the menu.
        print_option() -> None: Prints the available theme options for
                                the maze.
    """

    def get_title() -> str:
        return f"{Effect.BOLD}{Color.ORANGE}Theme Selector{Color.RESET}"

    def print_option() -> None:
        for key, value in dict_theme_data.items():
            str_temp = f"{value['color']}{key}. {value['name']}{Color.RESET}"
            print(f"║ {str_temp:70}║")

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
    elif int(user_choice) > 9 or int(user_choice) <= 0:
        print(f"\nInvalid theme, {user_choice} is not an option")
    else:
        theme = dict_theme_data[int(user_choice)]
        set_theme(color, Theme(theme.get("theme")))
    print(maze.show_maze())


def end_program() -> None:
    """
    End the program by printing a goodbye message and exiting with a
    status code of 2.
    """
    print("End of the program, bye !")
    exit(0)


# +-------------------------------------------------------------------------+
# |                                Variable                                 |
# +-------------------------------------------------------------------------+

dict_menu_data: dict[int, dict[str, str | Color | Callable]] = {
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
        "name": "Change maze ASCII",
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

dict_theme_data: dict[int, dict[str, str | Color | Theme | None]] = {
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

def manage_user_input(user_input: int, color: Dict[str, Color | str],
                      maze: Maze, config: dict) -> None:
    """
        Manage the user's menu selection by calling the corresponding function
        based on the input.

        Args:
            user_input (int): The number corresponding to the user's menu
                              choice.
            color (Dict[str, Color]): A dictionary containing the current
                                      color settings for the maze.
            maze (Maze): The maze object to be manipulated based on
                         the user's choice.
            config (dict): A configuration dictionary containing maze settings
                           that may be needed for certain functions.
    """
    if int(user_input) == 1:
        cast(Callable, dict_menu_data[1]["function"])(maze, config, color)
    elif int(user_input) == 2:
        cast(Callable, dict_menu_data[2]["function"])(maze, config)
    elif int(user_input) == 3:
        cast(Callable, dict_menu_data[3]["function"])(maze)
    elif int(user_input) == 4:
        cast(Callable, dict_menu_data[4]["function"])(maze, color)
    elif int(user_input) == 5:
        cast(Callable, dict_menu_data[5]["function"])()
    else:
        print(f"\nInvalid choice, {user_input} is not an option")


def print_menu(config: dict) -> None:
    """
    Print the menu to the console, displaying the available options for the
    user to interact with the maze.
    This function constructs a visually appealing menu using ASCII characters
    and colors.
    It displays the current seed used for maze generation and lists the
    available options for the user to choose from.

    Args:
        config (dict): A configuration dictionary containing settings.

    Method:
        get_title() -> str: Returns the title of the menu.
        print_option() -> None: Prints the available options for the
                                user to select from.
    """

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
    """
    Print the current seed used for maze generation to the console.

    Args:
        config (dict): A configuration dictionary containing the seed
                       information.
    """

    try:
        seedval = config["SEED"]
    except Exception:
        seedval = config["RANDOM_SEED"]

    print(f"Seed : {seedval}")


def get_random_color(color: Dict[str, Color | str]) -> None:
    """
    Generate random colors for the maze elements and update the color
    dictionary.
    This function randomly selects colors for the "STRICT", "WALL",
    "BLANK", and "SOLVE" elements of the maze. It ensures that the "BLANK"
    color is different from the other colors to maintain visibility.

    Args:
        color (Dict[str, Color]): A dictionary containing the current
        color settings, which will be updated with new random colors.
    """

    seed()
    color_list = list(Color)
    color["STRICT"] = choice(color_list).value
    color["WALL"] = choice(color_list).value
    color["BLANK"] = choice(color_list).value
    color["SOLVE"] = choice(color_list).value
    if color["BLANK"] in [color["WALL"], color["STRICT"], color["SOLVE"]]:
        get_random_color(color)
        return
    bg = str(color["BLANK"])
    bgval = bg[bg.index("[")+1]
    bgend = bg[bg.index("[")+2:len(bg)]
    bg = "\033[" + str(int(bgval) + 1) + bgend
    color["BLANK"] = bg
    color["SOLVE"] = str(color["SOLVE"]) + bg
    color["ENTRY"] = choice(color_list).value + bg
    color["EXIT"] = choice(color_list).value + bg


def init_color() -> dict[str, Color | str]:
    """
    Initialize the color settings for the maze by creating a dictionary
    with default color values for each maze element.

    Returns:
        Dict[str, Color]: A dictionary containing the initial color
                          settings.
    """
    color: dict[str, Color | str] = {"STRICT": Color.WHITE,
                                     "WALL": Color.WHITE,
                                     "ENTRY": Color.LIME,
                                     "EXIT": Color.RED,
                                     "BLANK": Color.BLACK,
                                     "SOLVE": Color.GOLD}
    return color


def set_theme(color: Dict[str, Color | str], theme: Theme) -> None:
    """
    Set the color settings for the maze based on a selected theme.
    This function updates the color settings for the maze elements according to
    the specified theme.

    Args:
        color (Dict[str, Color]): A dictionary containing the color settings.
        theme (Theme): The selected theme that contains the color settings.
    """
    color["STRICT"] = theme.value["STRICT"]
    color["WALL"] = theme.value["WALL"]
    color["BLANK"] = theme.value["BLANK"]
    bg = str(color["BLANK"])
    bgval = bg[bg.index("[")+1]
    bgend = bg[bg.index("[")+2:len(bg)]
    bg = "\033[" + str(int(bgval) + 1) + bgend
    color["BLANK"] = bg
    color["SOLVE"] = theme.value["SOLVE"].value + bg
    color["ENTRY"] = theme.value["ENTRY"].value + bg
    color["EXIT"] = theme.value["EXIT"].value + bg
