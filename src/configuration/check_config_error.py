# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  check_config_error.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 15:52:15 by alebaron        #+#    #+#               #
#  Updated: 2026/02/23 17:53:50 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +-------------------------------------------------------------------------+
# |                                 Import                                  |
# +-------------------------------------------------------------------------+


from src.utils.error import send_error, ConfigurationError
import re
from typing import Any


# +-------------------------------------------------------------------------+
# |                                Function                                 |
# +-------------------------------------------------------------------------+

def get_config(filename: str) -> dict:
    """
    Main entry point to retrieve and validate the maze configuration.

    Args:
        filename (str): The path to the configuration file.

    Returns:
        dict: A dictionary containing the parsed and validated configuration.
    """
    check_file(filename)
    required_config_format(filename)
    return required_config_key(filename)


def check_file(filename: str) -> None:
    """
    Checks if the file exists and is accessible.

    Args:
        filename (str): The path to the file to check.

    Raises:
        ConfigurationError: If the file is missing, inaccessible,
        or is a directory.
    """
    try:
        open(filename, "r")
    except FileNotFoundError:
        send_error(ConfigurationError(),
                   f"File \"{filename}\" not found. "
                   "Check the path and try again.")
    except PermissionError:
        send_error(ConfigurationError(), f"No permission to access {filename}."
                   " Check your access rights.")
    except IsADirectoryError:
        send_error(ConfigurationError(), f"Expected a file, but got directory "
                   f"{filename}. Please provide a file.")
    except Exception as e:
        send_error(ConfigurationError(), f"Unexcepted exception ({e}).")


def required_config_format(filename: str) -> None:
    """
    Verifies that every non-comment line follows the 'KEY=VALUE' format.

    Args:
        filename (str): The path to the configuration file.

    Raises:
        ConfigurationError: If a line does not match the required
        regex pattern.
    """
    with open(filename, "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        if line.startswith("#") or line == "":
            continue

        result = re.search("^[A-Z_]+=.+$", line)

        if result is None:
            send_error(ConfigurationError(), f"The line \"{line}\" does not "
                       f"comply with the format \"KEY=VALUE\".")


def required_config_key(filename: str) -> dict:
    """
    Parses the file, ensures all mandatory keys are present,
    and validates values.

    Mandatory keys: WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT.
    Also performs logic checks (e.g., entry and exit must not be
    identical or adjacent).

    Args:
        filename (str): The path to the configuration file.

    Returns:
        dict: The processed configuration dictionary.
    """
    dict_config: dict[str, Any] = {}
    key_required = {"WIDTH": False,
                    "HEIGHT": False,
                    "ENTRY": False,
                    "EXIT": False,
                    "OUTPUT_FILE": False,
                    "PERFECT": False
                    }

    with open(filename, "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        if line.startswith("#") or line == "":
            continue

        split_line = line.split("=")
        dict_config[split_line[0]] = split_line[1]

        for key in key_required:
            if (key == split_line[0]):
                key_required[key] = True

    for key in key_required:
        if key_required[key] is False:
            send_error(ConfigurationError(), f"Key \"{key}\" is missing in"
                       f" {filename}.")

    # Value Type Conversion and Range Validation
    dict_config["WIDTH"] = check_int_key("WIDTH",
                                         dict_config["WIDTH"], 5, None)
    dict_config["HEIGHT"] = check_int_key("HEIGHT",
                                          dict_config["HEIGHT"], 5, None)
    dict_config["ENTRY"] = check_coord_key("ENTRY", dict_config["ENTRY"],
                                           dict_config)
    dict_config["EXIT"] = check_coord_key("EXIT", dict_config["EXIT"],
                                          dict_config)
    dict_config["PERFECT"] = check_bool_key("PERFECT", dict_config["PERFECT"])

    check_file_key("OUTPUT_FILE", dict_config["OUTPUT_FILE"])

    # Logical validation: Entry vs Exit
    if (dict_config["EXIT"] == dict_config["ENTRY"]):
        send_error(ConfigurationError(), "Entry and Exit is at the "
                   "same place.")

    ex, ey = dict_config["ENTRY"]
    entry_adj = [(ex+1, ey), (ex-1, ey), (ex-1, ey+1), (ex-1, ey-1),
                 (ex+1, ey-1), (ex+1, ey+1), (ex, ey+1), (ex, ey-1)]

    if dict_config["EXIT"] in entry_adj:
        send_error(ConfigurationError(), "Entry and exit are adjacent.")

    dict_config["HIDE"] = True

    if "SEED" in dict_config:
        try:
            dict_config["SEED"] = int(dict_config["SEED"])
        except ValueError:
            send_error(ConfigurationError(), "SEED must be an integer.")

    return (dict_config)


def check_int_key(key: str, value: str, min: int, max: int | None) -> int:
    """
    Validates that a value is an integer and falls within the specified range.

    Args:
        key (str): The name of the configuration key.
        value (str): The string value to convert and check.
        min (int): The minimum allowed value.
        max (int | None): The maximum allowed value (None for no limit).

    Returns:
        int: The validated integer.
    """
    try:
        key_int = int(value)
        if min and min > key_int:
            raise ValueError(f"{key} must be greater than {min}")
        if max and max < key_int:
            raise ValueError(f"{key} must be lower than {max}")
    except Exception as e:
        send_error(ConfigurationError(), str(e))

    return key_int


def check_coord_key(key: str, value: str, dict_data: dict) -> tuple:
    """
    Validates coordinate strings (x,y) and ensures they
    fit within the maze dimensions.

    Args:
        key (str): The name of the coordinate key (e.g., 'ENTRY').
        value (str): The coordinate string (e.g., '10,5').
        dict_data (dict): The current config dict containing
        'WIDTH' and 'HEIGHT'.

    Returns:
        tuple: A tuple of (int, int) representing the coordinates.
    """
    split_int = value.split(",")

    if len(split_int) != 2:
        send_error(ConfigurationError(), f"{key} must contain coordinates "
                   "(E.g: 25,10)")

    try:
        x = int(split_int[0])
        y = int(split_int[1])
    except Exception:
        send_error(ConfigurationError(), f"{key} must be int,int")

    if x < 0 or x > dict_data["WIDTH"] - 1:
        send_error(ConfigurationError(), f"[{key}] x ({x}) must be > 0 and "
                   f"< {dict_data['WIDTH'] - 1}")

    if y < 0 or y > dict_data["HEIGHT"] - 1:
        send_error(ConfigurationError(), f"[{key}] y ({y}) must be > 0 and "
                   f"< {dict_data['HEIGHT'] - 1}")

    return (x, y)


def check_bool_key(key: str, value: str) -> bool:
    """
    Converts a configuration string into a boolean.

    Args:
        key (str): The name of the key.
        value (str): The string value ('True' or 'False').

    Returns:
        bool: The converted boolean value.
    """
    if value == "False":
        return False
    elif value == "True":
        return True
    else:
        send_error(ConfigurationError(), f"{key} must be True or False")
        return False


def check_file_key(key: str, value: str) -> None:
    """
    Ensures the provided value is a valid filename ending in '.txt'.

    Args:
        key (str): The name of the key.
        value (str): The filename string to validate.
    """
    regex = r"^[A-Za-z_]+\.txt$"
    result = re.search(regex, value)

    if result is None:
        send_error(ConfigurationError(), f"{key} must be a .txt filename")
