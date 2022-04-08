import re
padrao = re.compile("[0-9][,][0-1]?[0-9]")


def start_position(map: list) -> tuple:
    start_position = input(
        "Digite a posição inicial. Linha (0-9) x Coluna (0-19) Ex: 5,5 ")
