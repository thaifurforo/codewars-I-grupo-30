"""
Welcome to Cartography's Workshop!
"""


def print_map(map: list) -> None:
    for line in map:
        line_str = ''
        for char in line:
            line_str += char
        print(line_str)

    return None


def read_map_file() -> list:
    with open('map.txt', 'r') as file:
        maze = [[char for char in line] for line in file]
    for line in maze:
        if len(line) <= 20:
            break
        else:
            line.pop()

    return maze
