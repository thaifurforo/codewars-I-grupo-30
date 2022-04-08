import re
from turtle import position
global MAZE, PILE
MAZE = []
PILE = []

def read_map_file() -> list:

    with open('map.txt', 'r') as file:
        for line in file:
            MAZE.append(line.strip())

    return MAZE

def print_map() -> None:
    for line in MAZE:
        print(line)

    return None


def start_position() -> list:
    coordinate_pattern = re.compile("[0-9][,][0-1]?[0-9]")
    
    # validando formato
    while True:
        start_position = "1,2" #input("Digite a posição inicial. Linha (0-9) x Coluna (0-19) Ex: 5,5 ").strip()
        if not coordinate_pattern.fullmatch(start_position):
            print("Entrada inválida. Tente de novo.")
        
        # formato ok? validando espaço vazio
        else:
            coordinate = list(map(int, (start_position.split(","))))
            if MAZE[coordinate[0]][coordinate[1]] == " ":
                return coordinate
            else:
                print("Entrada inválida: local é uma parede. Tente de novo.")
        
    return list(coordinate)

def verify_surrounds() -> list:
    coordinate  = PILE[-1]
    rat_up = [coordinate[0] -1, coordinate[1]]
    rat_right = [coordinate[0], coordinate[1] + 1]
    rat_down = [coordinate[0] +1, coordinate[1]]
    rat_left = [coordinate[0], coordinate[1] - 1]
    directions = [rat_up, rat_right, rat_down, rat_left]

    #validar direções
    
    for destination in directions:
        if MAZE[destination[0]][destination[1]] == " ":
            return destination

def move() -> None:
    position  = PILE[-1]
    line_position = list(MAZE[position[0]])
    line_position[position[1]] = "."
    MAZE[position[0]] = "".join(line_position)

    destination = verify_surrounds()

    #MAZE[destination[0]][destination[1]] = "X"
    line_destination = list(MAZE[destination[0]])
    line_destination[destination[1]] = "X"
    MAZE[destination[0]] = "".join(line_destination)
    PILE.append(destination)
    
    

read_map_file()
PILE.append(start_position())

#while True:
for _ in range(5):
    print("Pilha: ", PILE)
    print_map()
    move()
    print()
