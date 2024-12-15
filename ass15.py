# assignment 15
import time
import math

# uitlezen text bestandje
with open('inputtest.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

class Coordinate:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self = (self.x,self.y)
    def __str__(self):
        return str((self.x,self.y))
    def __repr__(self):
        return str((self.x,self.y))

def getDirection(moveStr): # 0=up, 1=right, 2=down, 3=left
    if moveStr == "^":     return 0
    elif moveStr == ">":   return 1
    elif moveStr == "v":   return 2
    elif moveStr == "<":   return 3
    return -1

def checkMoveBoxSmall(move, location, warehouse):
    checklocation = Coordinate((location.x+int(math.fmod(move-1,2)),location.y+int(-math.fmod(move-2,2))))
    if warehouse[checklocation.x][checklocation.y] == "#":
        return False
    elif warehouse[checklocation.x][checklocation.y] == ".":
        return True
    elif warehouse[checklocation.x][checklocation.y] == "O":
        return checkMoveBoxSmall(move,checklocation,warehouse)
    else:
        return False # wel wack als het hier aankomt, want dan is de richting verandert op een manier

def moveBoxSmall(move, location, warehouse, countbox):
    checklocation = Coordinate((location.x+int(math.fmod(move-1,2)),location.y+int(-math.fmod(move-2,2))))
    if warehouse[checklocation.x][checklocation.y] == "O":
        countbox += 1
        return moveBoxSmall(move,checklocation,warehouse,countbox)
    elif warehouse[checklocation.x][checklocation.y] == ".":
        for n in range(countbox):
            warehouse[checklocation.x][checklocation.y] = "O"
            checklocation = Coordinate((checklocation.x-int(math.fmod(move-1,2)),checklocation.y-int(-math.fmod(move-2,2))))
            warehouse[checklocation.x][checklocation.y] = "."
        return warehouse
    else:
        return warehouse

# part 1
ts = time.time()
warehouse = []
moves = []
for line in input:
    if "#" in line:
        warehouse.append(list(line))
    elif line:
        moves.extend(list(line))
moves = [getDirection(move) for move in moves]
# for line in warehouse:
#     print("".join(line))
# print(moves)
start = [[Coordinate((c,r)) for c in range(len(warehouse[r])) if warehouse[r][c] == "@"] for r in range(len(warehouse)) if "@" in warehouse[r]][0][0]
location = start
for move in moves:
    checklocation = Coordinate((location.x+int(math.fmod(move-1,2)),location.y+int(-math.fmod(move-2,2))))
    if not warehouse[checklocation.x][checklocation.y] == "#":
        if warehouse[checklocation.x][checklocation.y] == ".":
            warehouse[location.x][location.y] = "."
            warehouse[checklocation.x][checklocation.y] = "@"       # we verplaatsten re robot ook fysiek op de map, zodat je makkelijk kan checken
            location = checklocation
        elif checkMoveBoxSmall(move, checklocation, warehouse):          # functie want er is wat recursion
            warehouse = moveBoxSmall(move,checklocation,warehouse,1)     # nieuwe functie want ik was lui
            warehouse[checklocation.x][checklocation.y] = "@"       # en dit gebeurt buiten de functie
            warehouse[location.x][location.y] = "."
            location = checklocation
    # print("Move " + str(move))
    # for line in warehouse:
    #     print("".join(line))
boxes = []
for r in range(len(warehouse)):
    boxes.extend([Coordinate((r,c)) for c in range(len(warehouse[r])) if warehouse[r][c] == "O"])
boxsumsmall = sum([100*box.x+box.y for box in boxes])
print("Deel 1 kostte " + str(time.time()-ts))                       # ongeveer 0.08s

# part 2
ts = time.time()
warehouseWident = []
moves = []
for line in input:
    if "#" in line:
        warehouseWident.append(list(line))
    elif line:
        moves.extend(list(line))
moves = [getDirection(move) for move in moves]
warehouseWide = []
for i in range(len(warehouseWident)):
    for j in range(len(warehouseWident[i])):
        if not warehouseWide:
            warehouseWide.append(["#","#"])
        elif warehouseWident[i][j] == "#":
            warehouseWide[len(warehouseWide)-1].extend(["#","#"])
        elif warehouseWident[i][j] == "O":
            warehouseWide[len(warehouseWide)-1].extend(["[","]"])
        elif warehouseWident[i][j] == ".":
            warehouseWide[len(warehouseWide)-1].extend([".","."])
        elif warehouseWident[i][j] == "@":
            warehouseWide[len(warehouseWide)-1].extend(["@","."])
        else:
            print("What the hell?")
    if i != len(warehouseWident)-1:
        warehouseWide.append([])
# for line in warehouseWide:
#         print("".join(line))
print("Deel 2 kostte " + str(time.time()-ts))

# printstatements for checking
# print(input)
# for line in warehouse:
#     print("".join(line))
# print(moves)

print("The boxsum for the small boxes is " + str(boxsumsmall))
