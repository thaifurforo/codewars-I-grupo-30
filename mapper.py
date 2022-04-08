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
