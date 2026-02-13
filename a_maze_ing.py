# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 15:30:12 by alebaron        #+#    #+#               #
#  Updated: 2026/02/13 12:53:24 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+

import sys
from src.maze.maze import Maze
from src.output.output import put_maze_val
from src.menu.menu import print_menu, manage_user_input
from src.menu.menu import get_random_color, init_color
from src.utils.error import print_error, send_error, MenuError
from src.configuration.check_config_error import get_config, ConfigurationError
from src.maze.generation import side_winder, hunt_and_kill


# +-------------------------------------------------------------------------+
# |                                  Main                                   |
# +-------------------------------------------------------------------------+

if __name__ == "__main__":

    # Get arguments
    argc = len(sys.argv)
    argv = sys.argv

    if (argc != 2):
        send_error(ConfigurationError(), "Wrong arguments. "
                   "Need one file.")

    color = init_color()
    get_random_color(color)
    # Configuration recovery
    config = get_config(argv[1])

    # Generating maze
    m = Maze(config["WIDTH"], config["HEIGHT"],
             config["ENTRY"], config["EXIT"], color)

    hunt_and_kill(m, config)

    # Displaying the maze
    m.show_maze()

    # Displaying the menu
    while (True):
        try:
            print_menu()
            user_input = input("Choice ? (1-5): ")
            if (user_input.isdigit() is False):
                print_error(MenuError(), "Bad Input, must be an integer (1-5)")
            else:
                manage_user_input(user_input, color)
                print()
                m.show_maze()

        except Exception as e:
            print(e)

        put_maze_val(m, config["OUTPUT_FILE"])
