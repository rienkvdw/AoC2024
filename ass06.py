# assignment 6 ik gebruik hier iets te veel extra libraries
import math
import copy
import time
import numpy as np
import itertools

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

maze = [list(line) for line in input]
# stroef maniertje om start te vinden
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "^":
            start = (i,j)

ts = time.time()
# part 1
path = copy.deepcopy(maze)
location = start
path[location[0]][location[1]] = "X"
steps = []
direction = 0       # 0=up, 1=right, 2=down, 3=left
done = False
while not done:     # we while looping today
    path[location[0]][location[1]] = "X"    # huidige locatie mag altijd een X worden
    # grote if, maar gewoon checken of de volgende waarde wel in de maze is
    if (0 <= location[0]+int(math.fmod(direction-1,2)) <= len(maze)-1) and (0 <= location[1]+int(-math.fmod(direction-2,2)) <= len(maze[location[0]])-1):
        # checken of er geen obstakel is
        if not maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] == "#":
            location = [location[0]+int(math.fmod(direction-1,2)),location[1]+int(-math.fmod(direction-2,2))]
            steps.append(location)
        else:
            # anders mooi draaien
            direction = (direction + 1)%4
    else:
        done = True
print("Deel 1 kostte " + str(time.time()-ts))

ts = time.time()
# part 2 gefaalde poging 1, wat een fucking mess van een code
# blocks = copy.deepcopy(maze)
# location = start
# direction = 0
# done = False
# while not done:     # we while looping today
#     if (0 <= location[0]+int(math.fmod(direction-1,2)) <= len(maze)-1) and (0 <= location[1]+int(-math.fmod(direction-2,2)) <= len(maze[location[0]])-1):
#         if not maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] == "#":
#             location = [location[0]+int(math.fmod(direction-1,2)),location[1]+int(-math.fmod(direction-2,2))]
#             checkDirection = (direction + 1)%4
#             checkLocation = start
#             if (0 <= location[0]+int(math.fmod(direction-1,2)) <= len(maze)-1) and (0 <= location[1]+int(-math.fmod(direction-2,2)) <= len(maze[location[0]])-1):
#                 match checkDirection:       # ik wist niet hoe ik dit ging doen zonder een losse case te maken per categorie, dus tijd voor 4 keer praktisch dezelfde code :)
#                     case 0:
#                         if any([1 for n in range(location[0],-1,-1) if maze[n][location[1]] == "#" ]):
#                             new_maze = copy.deepcopy(maze)
#                             new_maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "#"
#                             checkDirection = 0
#                             padje = np.zeros((len(maze), len(maze[0])))
#                             returned = False
#                             blocked = True
#                             while not (returned or not blocked):
#                                 if  (0 <= checkLocation[0]+int(math.fmod(checkDirection-1,2)) <= len(maze)-1) and \
#                                     (0 <= checkLocation[1]+int(-math.fmod(checkDirection-2,2)) <= len(maze[checkLocation[0]])-1):
#                                     if not new_maze[checkLocation[0]+int(math.fmod(checkDirection-1,2))][checkLocation[1]+int(-math.fmod(checkDirection-2,2))] == "#":
#                                         checkLocation = [checkLocation[0]+int(math.fmod(checkDirection-1,2)),checkLocation[1]+int(-math.fmod(checkDirection-2,2))]
#                                         if checkLocation == location and checkDirection == direction and padje[checkLocation[0]][checkLocation[1]] > 0:
#                                             returned = True
#                                         if padje[checkLocation[0]][checkLocation[1]] > 4:
#                                             blocked = False
#                                         else:
#                                             padje[checkLocation[0]][checkLocation[1]] += 1
#                                     else:
#                                         checkDirection = (checkDirection + 1)%4
#                                 else:
#                                     blocked = False
#                             if returned:
#                                 blocks[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "O"
#                     case 1:
#                         if any([1 for n in range(location[1],len(maze[location[1]]),1) if maze[location[0]][n] == "#" ]):
#                             new_maze = copy.deepcopy(maze)
#                             new_maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "#"
#                             checkDirection = 0
#                             padje = np.zeros((len(maze), len(maze[0])))
#                             returned = False
#                             blocked = True
#                             while not (returned or not blocked):
#                                 if  (0 <= checkLocation[0]+int(math.fmod(checkDirection-1,2)) <= len(maze)-1) and \
#                                     (0 <= checkLocation[1]+int(-math.fmod(checkDirection-2,2)) <= len(maze[checkLocation[0]])-1):
#                                     if not new_maze[checkLocation[0]+int(math.fmod(checkDirection-1,2))][checkLocation[1]+int(-math.fmod(checkDirection-2,2))] == "#":
#                                         checkLocation = [checkLocation[0]+int(math.fmod(checkDirection-1,2)),checkLocation[1]+int(-math.fmod(checkDirection-2,2))]
#                                         if checkLocation == location and checkDirection == direction and padje[checkLocation[0]][checkLocation[1]] > 0:
#                                             returned = True
#                                         if padje[checkLocation[0]][checkLocation[1]] > 4:
#                                             blocked = False
#                                         else:
#                                             padje[checkLocation[0]][checkLocation[1]] += 1
#                                     else:
#                                         checkDirection = (checkDirection + 1)%4
#                                 else:
#                                     blocked = False
#                             if returned:
#                                 blocks[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "O"
#                     case 2:
#                         if any([1 for n in range(location[0],len(maze),1) if maze[n][location[1]] == "#" ]):
#                             new_maze = copy.deepcopy(maze)
#                             new_maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "#"
#                             checkDirection = 0
#                             padje = np.zeros((len(maze), len(maze[0])))
#                             returned = False
#                             blocked = True
#                             while not (returned or not blocked):
#                                 if  (0 <= checkLocation[0]+int(math.fmod(checkDirection-1,2)) <= len(maze)-1) and \
#                                     (0 <= checkLocation[1]+int(-math.fmod(checkDirection-2,2)) <= len(maze[checkLocation[0]])-1):
#                                     if not new_maze[checkLocation[0]+int(math.fmod(checkDirection-1,2))][checkLocation[1]+int(-math.fmod(checkDirection-2,2))] == "#":
#                                         checkLocation = [checkLocation[0]+int(math.fmod(checkDirection-1,2)),checkLocation[1]+int(-math.fmod(checkDirection-2,2))]
#                                         if checkLocation == location and checkDirection == direction and padje[checkLocation[0]][checkLocation[1]] > 0:
#                                             returned = True
#                                         if padje[checkLocation[0]][checkLocation[1]] > 4:
#                                             blocked = False
#                                         else:
#                                             padje[checkLocation[0]][checkLocation[1]] += 1
#                                     else:
#                                         checkDirection = (checkDirection + 1)%4
#                                 else:
#                                     blocked = False
#                             if returned:
#                                 blocks[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "O"
#                     case 3:
#                         if any([1 for n in range(location[1],-1,-1) if maze[location[0]][n] == "#" ]):
#                             new_maze = copy.deepcopy(maze)
#                             new_maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "#"
#                             checkDirection = 0
#                             padje = np.zeros((len(maze), len(maze[0])))
#                             returned = False
#                             blocked = True
#                             while not (returned or not blocked):
#                                 if  (0 <= checkLocation[0]+int(math.fmod(checkDirection-1,2)) <= len(maze)-1) and \
#                                     (0 <= checkLocation[1]+int(-math.fmod(checkDirection-2,2)) <= len(maze[checkLocation[0]])-1):
#                                     if not new_maze[checkLocation[0]+int(math.fmod(checkDirection-1,2))][checkLocation[1]+int(-math.fmod(checkDirection-2,2))] == "#":
#                                         checkLocation = [checkLocation[0]+int(math.fmod(checkDirection-1,2)),checkLocation[1]+int(-math.fmod(checkDirection-2,2))]
#                                         if checkLocation == location and checkDirection == direction and padje[checkLocation[0]][checkLocation[1]] > 0:
#                                             returned = True
#                                         if padje[checkLocation[0]][checkLocation[1]] > 4:
#                                             blocked = False
#                                         else:
#                                             padje[checkLocation[0]][checkLocation[1]] += 1
#                                     else:
#                                         checkDirection = (checkDirection + 1)%4
#                                 else:
#                                     blocked = False
#                             if returned:
#                                 blocks[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] = "O"

#         else:
#             # anders mooi draaien
#             direction = (direction + 1)%4
#     else:
#         done = True

# part 2 poging 2
steps.sort()
steps = list(steps for steps,_ in itertools.groupby(steps)) # duplicates eruit halen
blocks = copy.deepcopy(maze)
for n in range(len(steps)):
    print("Step " + str(n) + " of " + str(len(steps)))
    location = start
    direction = 0
    new_maze = copy.deepcopy(maze)                          # oh boy, looping copy, ik hoop dat dat niet te veel tijd kost 
    new_maze[steps[n][0]][steps[n][1]] = "#"
    encountered = np.zeros((len(maze), len(maze[0])))
    loop = False
    while True:             # hier gebeurt hetzelfde als bij deel 1, maar neemt mee hoe vaak het over elk vakje komt
        if (0 <= location[0]+int(math.fmod(direction-1,2)) <= len(maze)-1) and (0 <= location[1]+int(-math.fmod(direction-2,2)) <= len(maze[location[0]])-1):
            if not new_maze[location[0]+int(math.fmod(direction-1,2))][location[1]+int(-math.fmod(direction-2,2))] == "#":
                encountered[location[0]][location[1]] += 1
                location = [location[0]+int(math.fmod(direction-1,2)),location[1]+int(-math.fmod(direction-2,2))]
                if  encountered[location[0]][location[1]] > 3:  # als dat vaak genoeg gebeurt, dan is er loop (bij 2 had ik een off by one error, dus we checken of het meer dan 3 is :)
                    loop = True
                    break
            else:
                # anders mooi draaien
                direction = (direction + 1)%4
        else:
            break
    if loop:
        blocks[steps[n][0]][steps[n][1]] = "O"
print("Deel 2 kostte " + str(time.time()-ts))


# printstatements for checking
# print(inputstring)

# print(maze)
# print(["".join(line) for line in path])
# print(["".join(line) for line in blocks])

print("The total of unsafe locations is " + str(sum(line.count("X") for line in path)))
print("The total of blocks is " + str(sum(line.count("O") for line in blocks)))