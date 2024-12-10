# assignment 10
import time
import numpy as np

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = list(inputstring.splitlines())
    heightmap = [list(map(int,list(line))) for line in input]
    heightmap = np.pad(heightmap,((1,1),(1,1)))

# magisch disfunctionele functie waarmee ik soort van het juiste kan doen
def findTops(ls,m,n):
    tops = []
    for l in ls:
        for i in range(ls[0]-1,ls[0]+2):
            for j in range(ls[1]-1,ls[1]+2):
                if (i != ls[0] and j == ls[1]) or (i == ls[0] and j != ls[1]):
                    if m[i][j] == n+1:
                        if m[i][j] == 9:
                            tops.append((i,j))
                        else:
                            tops.extend(findTops((i,j),m,n+1))
    return tops

# part 1 and 2
ts = time.time()
zeroes = []
for i in range(1,len(heightmap)-1):
    for j in range(1,len(heightmap[0])-1):
        if heightmap[i][j] == 0:
            zeroes.append((i,j))

trailheadscores = np.zeros(len(zeroes))
trailheadratings = np.zeros(len(zeroes))
for n in range(len(zeroes)):
    tops = findTops(zeroes[n],heightmap,0)
    trailheadscores[n] = int(len(set(tops)))    # met set heb je alle unieke units eruit, dus dit werkt
    trailheadratings[n] = int(len(tops)/512)    # er gebeurt iets magisch waardoor al mijn lijsten 512 keer hetgene zijn wat het moet zijn. Ik kan niet vinden waarom. Beun tijd

print("Deel 1 en 2 kostten " + str(time.time()-ts))

# printstatements for checking
# print(heightmap)
# print(zeroes)

print("The total score is " + str(int(sum(trailheadscores))))
print("The total rating is " + str(int(sum(trailheadratings))))