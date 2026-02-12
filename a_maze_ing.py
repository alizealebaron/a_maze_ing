# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron, tcolson                         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 15:30:12 by alebaron        #+#    #+#               #
#  Updated: 2026/02/12 14:30:50 by tcolson         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from src.maze.maze import Maze
from src.output.output import put_maze_val
from src.maze.generation import new


m = Maze(19, 14, (0, 0), (5, 2))
try:
    # m.change_cell((2, 1), Cell.BLANK)
    # m.change_cell((3, 1), Cell.BLANK)
    new(m)
    m.show_maze()
except Exception as e:
    print(e)

put_maze_val(m, "test.txt")
