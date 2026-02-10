clean :
	@find . | grep -E "__pycache__" | xargs rm -rf


run : a_maze_ing.py
	@python3 a_maze_ing.py