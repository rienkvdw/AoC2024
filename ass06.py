# assignment 5
import math

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

maze = [list(line) for line in input]
# stroef maniertje om start te vinden
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "^":
            start = [i,j]

# part 1
path = maze
location = start
path[location[0]][location[1]] = "X"
direction = 0
done = False
while not done:     # we while looping today
    path[location[0]][location[1]] = "X"    # huidige locatie mag altijd een X worden
    # grote if, maar gewoon checken of de volgende waarde wel in de maze is
    if (0 <= location[0]+int(math.fmod(direction-1,2)) <= len(maze)-1) and (0 <= location[1]+int(-math.fmod(direction-2,2)) <= len(maze[location[0]])-1):
        # checken of er geen obstakel is
        if not maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] == "#":
            location = [location[0]+int(math.fmod(direction-1,2)),location[1]+int(-math.fmod(direction-2,2))]
        else:
            # anders mooi draaien
            direction = (direction + 1)%4
    else:
        done = True

# part 2
# ik weet nog niet hoe ik dit ga doen

# printstatements for checking
# print(inputstring)

# print(maze)
# print(path)
print("The total of unsafe locations is " + str(sum(line.count("X") for line in path)))