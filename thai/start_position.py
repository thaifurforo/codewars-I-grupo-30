import re
padrao = re.compile("[0-9][,][0-1]?[0-9]")


# Esboço do japa:
def start_position(lab_map: list) -> tuple:
    coordinate_pattern = re.compile("[0-9][,][0-1]?[0-9]")

    # validando formato
    while True:
        start_position = input(
            "Digite a posição inicial. Linha (0-9) x Coluna (0-19) Ex: 5,5 ").strip()
        if not coordinate_pattern.fullmatch(start_position):
            print("Entrada inválida. Tente de novo.")

        # formato ok? validando espaço vazio
        else:
            coordinate = tuple(map(int, (start_position.split(","))))
            if lab_map[coordinate[0]][coordinate[1]] == " ":
                return coordinate
            else:
                print("Entrada inválida: local é uma parede. Tente de novo.")

    return tuple(coordinate)
