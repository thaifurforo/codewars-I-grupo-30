from start_position import *
from mapper import *
from move import *
"""
Project name suggestion: A Maze Game
"""


def main():
    maze = read_map_file()
    print_map(maze)
    start_at = start_position(maze)
    maze[start_at[0]][start_at[1]] = 'X'
    pile = [start_at]
    move(start_at, maze, pile)


if (__name__ == '__main__'):
    main()
