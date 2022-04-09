from mapper import print_map


def verify_surrounds(current_position: tuple, maze: list) -> list:
    maze_height = len(maze)
    maze_width = len(maze[0])

    position_north = [current_position[0] - 1, current_position[1]]
    position_south = [current_position[0] + 1, current_position[1]]
    position_east = [current_position[0], current_position[1] + 1]
    position_west = [current_position[0], current_position[1] - 1]

    if not (position_north[0] <= maze_height and position_north[0] >= 0):
        position_north = [0, 0]
    if not (position_south[0] <= maze_height and position_south[0] >= 0):
        position_south = [0, 0]
    if not (position_east[1] <= maze_width and position_east[1] >= 0):
        position_east = [0, 0]
    if not (position_west[1] <= maze_width and position_west[1] >= 0):
        position_west = [0, 0]

    surround_pos = [position_north, position_south,
                    position_east, position_west]

    surround_chars = [maze[surround_pos[0][0]][surround_pos[0][1]], maze[surround_pos[1][0]][surround_pos[1]
                                                                                             [1]], maze[surround_pos[2][0]][surround_pos[2][1]], maze[surround_pos[3][0]][surround_pos[3][1]]]

    return surround_pos, surround_chars


def move(current_position: tuple, maze: list, moves_stack: list):
    valid_position = False

    surround_position, surround_chars = verify_surrounds(
        current_position, maze)

    index = 0

    while valid_position == False and index <= 3:
        testing_position = surround_chars[index]
        if testing_position == 'S':
            maze[surround_position[index][0]][surround_position[index][1]] = 'X'
            maze[current_position[0]][current_position[1]] = '.'
            valid_position = True
            print_map(maze)
            print('Vitória')
        elif testing_position == ' ':
            valid_position = True
            maze[surround_position[index][0]][surround_position[index][1]] = 'X'
            maze[current_position[0]][current_position[1]] = '.'
            current_position = surround_position[index]
            moves_stack.append(current_position)
            print_map(maze)
            move(current_position, maze, moves_stack)
            return None
        else:
            index += 1

    if not valid_position:
        possible_step = any(
            [True if char == ' ' else False for char in surround_chars])
        pos = len(moves_stack)
        index = -1
        while not possible_step:
            last_position = moves_stack[index]
            surround_chars = verify_surrounds(last_position, maze)[1]
            possible_step = any(
                [True if char == ' ' else False for char in surround_chars])
            maze[last_position[0]][last_position[1]] = 'X'
            if index != -1:
                print_map(maze)
            maze[last_position[0]][last_position[1]] = '.'
            index -= 1

        moves_stack[:pos+index]

        maze[last_position[0]][last_position[1]] = 'X'
        maze[moves_stack[-1][0]][moves_stack[-1][1]] = '.'

        move(last_position, maze, moves_stack)
