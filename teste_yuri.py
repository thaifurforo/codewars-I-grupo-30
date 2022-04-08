import re
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
                line_position = list(MAZE[coordinate[0]])
                line_position[coordinate[1]] = "X"
                MAZE[coordinate[0]] = "".join(line_position)
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
    rat_position  = PILE[-1]
    line_position = list(MAZE[rat_position[0]])
    line_position[rat_position[1]] = "."
    MAZE[rat_position[0]] = "".join(line_position)

    rat_destination = verify_surrounds()

    #MAZE[destination[0]][destination[1]] = "X"
    line_destination = list(MAZE[rat_destination[0]])
    line_destination[rat_destination[1]] = "X"
    MAZE[rat_destination[0]] = "".join(line_destination)
    PILE.append(rat_destination)
    
    

read_map_file()
PILE.append(start_position())


#while True:
for _ in range(4):
    print("Pilha: ", PILE)
    print_map()
    move()
    print()
