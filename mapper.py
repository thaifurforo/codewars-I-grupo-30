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


"""
Yuri - opinião sobre alteração:

def print_map(lab_map: list) -> None:
    for line in lab_map:
        print(line)

    return None


def read_map_file() -> list:
    lab_map = []
    with open('map.txt', 'r') as file:
        for line in file:
            lab_map.append(line.strip())

    return lab_map

"""