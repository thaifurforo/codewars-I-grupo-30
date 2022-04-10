from random import randint
import mapper

def maze_generator():
    maze_size = (randint(9, 50), randint(19, 100))
    wall_ratio = 0.64
    space_ratio = 1 - wall_ratio

    maze = []
    for l in range(maze_size[0]):
        sublist = []
        for c in range(maze_size[1]):
            sublist.append('#')
        maze.append(sublist)

    total = maze_size[0] * maze_size[1]
    space = 0


    exit_block = (randint(1, maze_size[0] - 1), maze_size[1])
    maze[exit_block[0]][exit_block[1]] = "S"
    space += 1

    start_pos = (exit_block[0],exit_block[1] - 1)
    for _ in range(50):
        line_or_column = False

        if randint(1,2) % 2 == 0:
            line_or_column = True
        
        if line_or_column:
            

    while 1:
        line_or_column = False

        if randint(1,2) % 2 == 0:
            line_or_column = True

        if line_or_column:
            p1 = randint(1, maze_size[0] - 2)
            p2 = randint(1, maze_size[0] - 2)
            p3 = randint(1, maze_size[1] - 2)

            for l in range(abs(p1-p2)):
                maze[l][p3] = ' '
                space += 1
        else:
            p1 = randint(1, maze_size[1] - 2)
            p2 = randint(1, maze_size[1] - 2)
            p3 = randint(1, maze_size[0] - 2)

            for c in range(abs(p1-p2)):
                maze[p3][c] = ' '
                space += 1
        
        ratio = space/total
        if ratio >= space_ratio:
            break

    mapper.print_map(maze)
    
maze_generator()