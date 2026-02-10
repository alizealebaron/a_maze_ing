# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 15:30:12 by alebaron        #+#    #+#               #
#  Updated: 2026/02/10 17:00:55 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from src.maze.maze import Maze, Cell
from src.output.output import put_maze_val


m = Maze(19, 14, (0, 0), (5, 2))
try:
    # m.change_cell((2, 1), Cell.BLANK)
    # m.change_cell((3, 1), Cell.BLANK)
    m.show_maze()
    m.change_cell((8, 3), Cell.BLANK)
except Exception as e:
    print(e)

put_maze_val(m, "test.txt")
