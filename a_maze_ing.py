# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 15:30:12 by alebaron        #+#    #+#               #
#  Updated: 2026/02/23 11:23:38 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+

import sys
import os
from src.maze.maze import Maze
from src.output.output import put_maze_val
from src.menu.menu import print_menu, manage_user_input
from src.menu.menu import get_random_color, init_color
from src.utils.error import print_error, send_error, MenuError
from src.configuration.check_config_error import get_config, ConfigurationError
from src.maze.generation import hunt_and_kill
from src.maze.resolution import resolution


# +-------------------------------------------------------------------------+
# |                                  Main                                   |
# +-------------------------------------------------------------------------+

if __name__ == "__main__":

    """
    The main function of the program. It is responsible for:
    - Getting the arguments from the command line
    - Recovering the configuration from the file
    - Generating the maze
    - Searching for the solution
    - Generating the output file
    - Displaying the menu

    It also handles the KeyboardInterrupt exception to display a custom message
    when the user interrupts the program.
    """

    try:
        # Get arguments
        argc = len(sys.argv)
        argv = sys.argv

        if (argc != 2):
            send_error(ConfigurationError(), "Wrong arguments. "
                       "Need one file.")

        color = init_color()
        get_random_color(color)

        color = init_color()
        get_random_color(color)
        # Configuration recovery
        config = get_config(argv[1])

        # Generating maze
        maze = Maze(config["WIDTH"], config["HEIGHT"],
                    config["ENTRY"], config["EXIT"], color)

        hunt_and_kill(maze, config)

        # Searching for solution
        path = resolution(maze, config)

        # Generating output
        put_maze_val(maze, config["OUTPUT_FILE"], path)

        # Displaying the menu
        i = 0
        while (True):
            try:
                print_menu(config)
                user_input = input("Choice ? (1-5): ")
                os.system("clear")
                if (user_input.isdigit() is False):
                    print_error(MenuError(), "Bad Input, "
                                + "must be an integer (1-5)")
                else:
                    manage_user_input(user_input, color, maze, config)
                    print()

            except Exception as e:
                print(e)

    except KeyboardInterrupt:
        os.system("clear")
        file = open("src/utils/interrupt.txt", "r", encoding='utf-8')
        content = file.read()
        print(content)
