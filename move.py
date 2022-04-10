from random import choice
from mapper import print_map


def find_exit(current_position: tuple, maze: list) -> None:
    """
    Makes the robot try to find the exit of the Maze.
    """
    moves_stack = [current_position]

    while True:

        possible_destinations = verify_surrounds(current_position, maze)

        if possible_destinations and possible_destinations[0] == 'Win':
            move(current_position, possible_destinations[1], maze)
            print("Vitória!")
            break

        elif possible_destinations:
            destination = choice(possible_destinations)
            move(current_position, destination, maze)
            moves_stack.append(destination)
            current_position = destination

        else:
            last_position = moves_stack.pop()
            move(current_position, last_position, maze)
            current_position = last_position


def move(current_position: tuple, destination: tuple, maze: list) -> list:
    """
    Moves the robot through the maze.
    """
    maze[current_position[0]][current_position[1]] = '.'
    maze[destination[0]][destination[1]] = 'X'

    print_map(maze)

    return maze


def verify_surrounds(current_position: tuple, maze: list) -> list:
    """
    Verifies possible next steps to the robot.
    """
    north = (current_position[0] - 1, current_position[1])
    south = (current_position[0] + 1, current_position[1])
    east = (current_position[0], current_position[1] + 1)
    west = (current_position[0], current_position[1] - 1)

    positions = {
        north: maze[north[0]][north[1]],
        south: maze[south[0]][south[1]],
        east: maze[east[0]][east[1]],
        west: maze[west[0]][west[1]]
    }

    possible_destinations = []

    for position, character in positions.items():
        # If the robot finds the Exit, that will be the only possible destination
        if character == 'S':
            return ['Win', position] 
        elif character == ' ':
            possible_destinations.append(position)   

    return possible_destinations
