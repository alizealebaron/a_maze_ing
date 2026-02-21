# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  error.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 16:02:31 by alebaron        #+#    #+#               #
#  Updated: 2026/02/21 17:10:51 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                                  Class                                  |
# +-------------------------------------------------------------------------+


class ConfigurationError(Exception):
    """
    Exception raised for errors in the configuration.
    """
    pass


class MenuError(Exception):
    """
    Exception raised for errors in the menu.
    """
    pass


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def send_error(error_type: Exception, message: str) -> None:
    """
    Print an error message and exit the program.

    Args:
        error_type (Exception): The type of error to be printed.
        message (str): The error message to be printed.
    """
    print(f"{error_type.__class__.__name__}: {message}")
    exit(2)


def print_error(error_type: Exception, message: str) -> None:
    """
    Print an error message without exiting the program.
    Args:
        error_type (Exception): The type of error to be printed.
        message (str): The error message to be printed.
    """
    print(f"{error_type.__class__.__name__}: {message}")
