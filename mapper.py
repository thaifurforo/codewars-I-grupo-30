"""

"""
import os
from time import sleep

def print_map(maze: list) -> None:
    """
    Prints the map.
    """

    sleep(0.3)  # Esperar por 0.3 segundos
    os.system('cls')

    for line in maze:
        line_str = ''
        for char in line:
            line_str += char
        print(line_str)

    return None


def read_map_file() -> list:
    """
    Reads the file with the map.
    """
    with open('map.txt', 'r') as file:
        maze = [[char for char in line] for line in file]
    for line in maze:
        if len(line) <= 20:
            break
        else:
            line.pop()

    return maze
