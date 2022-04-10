import mapper

maze = mapper.read_map_file()

space_char = 0
wall_char = 0

for sublist in maze:
    for char in sublist:
        if (char == " " or char == "S"):
            space_char += 1
        else:
            wall_char += 1


ratio_space = space_char/(len(maze) * len(maze[0]))
ratio_wall = 1 - ratio_space

print(ratio_space)
print(ratio_wall)
