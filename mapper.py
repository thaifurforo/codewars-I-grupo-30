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


# opinião sobre mudanças:
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

# sugestão thai - pra que crie lista de listas que fica mais fácil de buscar o index quando fizer o move. a impressão está fazendo caracter a caracter, aí mesmo sendo listas de listas fica bonita no print


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
