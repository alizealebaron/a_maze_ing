# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  check_config_error.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 15:52:15 by alebaron        #+#    #+#               #
#  Updated: 2026/02/09 16:44:10 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                               Importation                               |
# +-------------------------------------------------------------------------+


from utils.error import send_error, ConfigurationError


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def check_file(filename: str) -> None:

    try:
        open(filename, "r")
    except FileNotFoundError:
        send_error(ConfigurationError,
                   f"File \"{filename}\" not found. "
                   "Check the path and try again.")
    except PermissionError:
        send_error(ConfigurationError, f"No permission to access {filename}."
                   " Check your access rights.")
    except IsADirectoryError:
        send_error(ConfigurationError, f"Expected a file, but got directory "
                   f"{filename}. Please provide a file.")
    except Exception:
        send_error(ConfigurationError, "Unexcepted exception.")
