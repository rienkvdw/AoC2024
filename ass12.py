# assignment 12
import time
import numpy as np
import copy

# uitlezen text bestandje
with open('inputtest.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    garden = [list(line) for line in input]
    garden = np.pad(garden,((1,1),(1,1)))

# damn look at all these functions
# vind per plant alle locaties 
def findPlants(garden):
    plants = {}
    for i in range(1,len(garden)-1):
        for j in range(1,len(garden[i])-1):
            if garden[i][j] in plants:
                plants[garden[i][j]] += [(i,j)]
            else:
                plants[garden[i][j]] = [(i,j)]
    return plants

# simpele check om te vinden of een locatie naast iets van een regio ligt
def checkAdjacent(location, region):
    for locs in region:
        if  (abs(location[0]-locs[0]) == 1 and abs(location[1]-locs[1]) == 0) or \
            (abs(location[1]-locs[1]) == 1 and abs(location[0]-locs[0]) == 0):
            return True
    return False

# merge regions (voor het regio vinden ding)
def mergeRegions(regions):
    new_regions = copy.deepcopy(regions)    # dit maakt het waarschijnlijk erg traag, maar dont care
    changes = False
    for n in range(len(regions)):
        for m in range(n+1,len(regions)):
            for i in range(len(regions[n])):
                if checkAdjacent(regions[n][i], regions[m]):
                    new_regions.remove(regions[n])
                    new_regions.remove(regions[m])
                    new_regions.append(regions[n] + regions[m])
                    new_regions = mergeRegions(new_regions)
                    break
            else:
                continue
            break
        else:
            continue
        break
    return new_regions

# vind alle regio's
def findRegions(plants):
    regions = []
    for planttype in plants:
        regionsPlant = []
        for location in plants[planttype]:
            if not regionsPlant:
                regionsPlant.append([location])
            else:
                added = False
                for n in range(len(regionsPlant)):
                    if checkAdjacent(location, regionsPlant[n]):
                        regionsPlant[n].extend([location])
                        added = True
                        break
                if not added:
                    regionsPlant.append([location])
        regions.extend(mergeRegions(regionsPlant))
    return regions

# berekent de perimeters van alle regio's
def findPerimeters(regions):
    perimeters = []
    for region in regions:
        perimeter = 0
        for location in region:     # hele domme set aan ifstatements, maar dit is niet hetgene wat het langzaam maakt
            if (location[0]-1,location[1]) not in region:
                perimeter += 1
            if (location[0]+1,location[1]) not in region:
                perimeter += 1
            if (location[0],location[1]-1) not in region:
                perimeter += 1
            if (location[0],location[1]+1) not in region:
                perimeter += 1
        perimeters.append(perimeter)
    return perimeters

# part 1 bijna alles gebeurt nu met functies (behalve de oneliner voor area) dus dit deel is vrij kort
ts = time.time()
plants = findPlants(garden)
regions = findRegions(plants)
areas = [len(x) for x in regions]
perimeters = findPerimeters(regions)
print("Deel 1 kostte " + str(time.time()-ts))       # duurt zo'n 10 seconden 

# voor deel 2 de placeholder functie die nodig gaat zijn, alle eerdere code zou herbruikmaar moeten zijn
def findSides(regions):
    sides = []
    for region in regions:
        side = 1
        sides.append(side)
    return sides

# part 2 
ts = time.time()
sides = findSides(regions)
print("Deel 2 kostte " + str(time.time()-ts))

# printstatements for checking
# print(garden)
# print(plants)
# print(regions)

# print(areas)
# print(perimeters)
print("The total price for part 1 is " + str(sum([areas[n]*perimeters[n] for n in range(len(areas))])))
print("The total price for part 2 is " + str(sum([areas[n]*sides[n] for n in range(len(areas))])))