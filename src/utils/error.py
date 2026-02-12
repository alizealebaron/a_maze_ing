# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  error.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 16:02:31 by alebaron        #+#    #+#               #
#  Updated: 2026/02/12 12:28:34 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                                  Class                                  |
# +-------------------------------------------------------------------------+


class ConfigurationError(Exception):
    pass


class MenuError(Exception):
    pass


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def send_error(error_type: Exception, message: str) -> None:
    print(f"{error_type.__class__.__name__}: {message}")
    exit(2)


def print_error(error_type: Exception, message: str) -> None:
    print(f"{error_type.__class__.__name__}: {message}")
