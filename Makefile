# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Makefile                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 14:14:12 by alebaron        #+#    #+#               #
#  Updated: 2026/02/16 14:21:23 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# ==========================
#         Variables
# ==========================

VENV_PATH = .venv
VENV_PYTHON = $(VENV_PATH)/bin/python3
VENV_PIP = $(VENV_PATH)/bin/pip

MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports \
			 --disallow-untyped-defs --check-untyped-defs

CONFIG = default_config.txt

# ==========================
#           Colors
# ==========================

BLACK   := \033[30m
RED     := \033[31m
GREEN   := \033[32m
YELLOW  := \033[33m
BLUE 	:= \033[96m
MAGENTA := \033[38;5;206m
CYAN    := \033[36m
WHITE   := \033[37m
RESET   := \033[0m
BOLD    := \033[1m
DIM     := \033[2m
ITALIC  := \033[3m
UNDER   := \033[4m
BLINK   := \033[5m
REVERSE := \033[7m
HIDDEN  := \033[8m
PINK 	:= \033[35m

# ==========================
#           Rules
# ==========================

install:
	

clean :
	@find . | grep -E "__pycache__" | xargs rm -rf


run : a_maze_ing.py
	@python3 a_maze_ing.py
