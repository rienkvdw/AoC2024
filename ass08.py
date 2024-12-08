# assignment 8
import numpy as np
import time

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    city = [list(line) for line in input]

# lelijke for loop om alle antenna locaties te vinden
antennas = {}
for i in range(len(city)):
    for j in range(len(city[0])):
        if city[i][j] != ".":
            if city[i][j] not in antennas:
                antennas[city[i][j]] = [(i,j)]
            else:
                antennas[city[i][j]] += [(i,j)]

# functie voor checken of het wel in het veld is
def inRange(loc,city):
    if 0 <= loc[0] < len(city) and 0 <= loc[1] < len(city[0]):
        return True 
    else:
        return False

# functie voor antinodes vinden ZONDER harmonics
def findAntinode(loc1, loc2,city):
    antinodes = []
    anti = (2*loc1[0]-loc2[0],2*loc1[1]-loc2[1])    # ene kant op checken
    if inRange(anti,city):
        antinodes += [anti]
    anti = (2*loc2[0]-loc1[0],2*loc2[1]-loc1[1])    # andere kant op checken
    if inRange(anti,city):
        antinodes += [anti]
    return antinodes

# part 1
ts = time.time()
antinodes1 = [["." for x in range(len(city[0]))] for y in range(len(city))]
for locations in antennas.values():                     # per soort antenna loopen
    for loc1 in locations:                              # waarschijnlijk kunnen deze eerste twee for loops beter
        for loc2 in locations:
            if loc1 != loc2:
                nodes = findAntinode(loc1,loc2,city)    # alle nodes van de functie pakken en hekjes maken
                for node in nodes:
                    antinodes1[node[0]][node[1]] = "#"

print("Deel 1 kostte " + str(time.time()-ts))           # iets meer dan een halve ms

# functie voor antinodes vinden met harmonics, waarschijnlijk kan die shit in 1 for loop but I couldnt be bothered
def findAntinodeHarmonics(loc1, loc2,city):
    antinodes = []
    for n in range(0,len(city)):                        # ene kant op checken
        anti = (loc1[0]-n*(loc2[0]-loc1[0]),loc1[1]-n*(loc2[1]-loc1[1]))
        if inRange(anti,city):
            antinodes += [anti]
        else:
            break
    for n in range(0,len(city)):                        # andere kant op checken
        anti = (loc2[0]-n*(loc1[0]-loc2[0]),loc2[1]-n*(loc1[1]-loc2[1]))
        if inRange(anti,city):
            antinodes += [anti]
        else:
            break
    return antinodes

# part 2
ts = time.time()
antinodes2 = [["." for x in range(len(city[0]))] for y in range(len(city))]
for locations in antennas.values():                     # per soort antenna loopen
    for loc1 in locations:
        for loc2 in locations:
            if loc1 != loc2:                            # poah harmonic antinodes vinden
                nodes = findAntinodeHarmonics(loc1,loc2,city)
                for node in nodes:
                    antinodes2[node[0]][node[1]] = "#"
print("Deel 2 kostte " + str(time.time()-ts))           # rond 2.5ms

# printstatements for checking
# print(input)

# print(antennas)
# for line in antinodes2:
#     print("".join(line))

print("The total of antinode locations is " + str(sum([line.count("#") for line in antinodes1])))
print("The total of antinode locations with harmonics is " + str(sum([line.count("#") for line in antinodes2])))