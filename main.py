from start_position import *
from mapper import *
from move import *


"""
Project name suggestion: A Maze Game
"""

moves_stack = []


def main():
    maze = read_map_file()
    current_position = start_position(maze)
    moves_stack = [current_position]
    move(current_position, maze, moves_stack)


if (__name__ == '__main__'):
    main()
