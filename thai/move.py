from mapper import *
from start_position import *


def move(current_position: tuple, maze: list, pile: list, movimentos: int = 0) -> None:

    if current_position[0] <= 9 and 0 <= current_position[1]+1 <= 19:
        p1 = (current_position[0], current_position[1]+1)
    else:
        p1 = (0, 0)

    if 0 <= current_position[0]-1 <= 9 and 0 <= current_position[1] <= 19:
        p2 = (current_position[0]-1, current_position[1])
    else:
        p2 = (0, 0)

    if 0 <= current_position[0] <= 9 and 0 <= current_position[1]-1 <= 19:
        p3 = (current_position[0], current_position[1]-1)
    else:
        p3 = (0, 0)

    if 0 <= current_position[0]+1 <= 9 and 0 <= current_position[1] <= 19:
        p4 = (current_position[0]+1, current_position[1])
    else:
        p4 = (0, 0)

    possible_next_positions = [p1, p2, p3, p4]

    index = 0

    continue_maze = True

    valid_position = False

    while not valid_position and index <= 3:
        next_position = possible_next_positions[index]
        if maze[next_position[0]][next_position[1]] == 'S':
            movimentos += 1
            maze[next_position[0]][next_position[1]] = 'X'
            maze[current_position[0]][current_position[1]] = '.'
            print_map(maze)
            print(
                f'\n*O robô encontrou a saída após {movimentos} movimentos!*')
            continue_maze = False
            break
        elif maze[next_position[0]][next_position[1]] == ' ':
            movimentos += 1
            valid_position = True
            maze[current_position[0]][current_position[1]] = '.'
            maze[next_position[0]][next_position[1]] = 'X'
            pile.append(next_position)
            current_position = next_position
            print_map(maze)
            print('\n')
            break
        else:
            index += 1

    if valid_position and continue_maze:
        move(current_position, maze, pile, movimentos)
    elif not valid_position and continue_maze:
        maze[current_position[0]][current_position[1]] = '.'
        current_position = pile.pop()
        movimentos += 1
        move(current_position, maze, pile, movimentos)
    else:
        pass
