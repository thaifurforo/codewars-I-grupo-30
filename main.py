from start_position import *
from mapper import *
from move import *

"""
Project name suggestion: A Maze Game
"""


def main():
    maze = read_map_file()
    current_position = start_position(maze)
    find_exit(current_position, maze)


if (__name__ == '__main__'):
    main()
