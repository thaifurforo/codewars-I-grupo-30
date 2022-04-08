"""
Welcome to Cartography's Workshop!
"""


def print_map(map: list) -> None:
    for line in map:
        print(line)

    return None


def read_map_file() -> list:
    with open('map.txt', 'r') as file:
        for line in file:
            map.append(line.strip())

    return map




#opinião sobre mudanças:
def read_map_file() -> list:
    global MAZE
    MAZE = []

    with open('map.txt', 'r') as file:
        for line in file:
            MAZE.append(line.strip())

    return MAZE

def print_map() -> None:
    for line in MAZE:
        print(line)

    return None

