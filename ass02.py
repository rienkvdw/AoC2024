# assignment 2

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# N inputs
reports = []
for lines in input:                     # splitten op spaties en zetten in de losse waardes
    levels = [int(x) for x in lines.split(" ") if x]
    reports.append(levels)

# part 1
safeness1 = len(reports)
for levels in reports:
    creasity = (levels[1]-levels[0])    # eerste verschil pakken als ding of het afneemt of toeneemt
    if creasity == 0:                   # als eerste al geen verschil heeft kan het gewoon weg
        safeness1 -= 1
    else:
        creasity /= abs(creasity)       # -1 of 1, geeft aan of het toeneemt of afneemt, zodat je kan checken of dat constant blijft
                                        # in goede geval zou altijd 1, 2 of 3 moeten zijn (decrease is min * min)
        safeness1 -= any([1 for i in range(0,len(levels)-1) if not (1 <= creasity*(levels[i+1]-levels[i]) <= 3)])

# part 2 
safeness2 = len(reports)
for levels in reports:
    safe = True                         # we doen hier eerst nog heel lelijk hetzelfde als voor de eerste, want anders hoeft het nog ergere van deel 2 niet
    creasity = (levels[1]-levels[0])    # eerste verschil pakken als ding of het afneemt of toeneemt
    if creasity == 0:                   # als eerste al geen verschil heeft kan je er gewoon uit
        safe = False
    else:
        creasity /= abs(creasity)       # -1 of 1, geeft aan of het toeneemt of afneemt, zodat je kan checken of dat constant blijft
                                        # in goede geval zou altijd 1, 2 of 3 moeten zijn (decrease is min * min)
        safe = not any([1 for i in range(0,len(levels)-1) if not (1 <= creasity*(levels[i+1]-levels[i]) <= 3)]) 
    if not safe:                        # kut het is niet veilig, nou dan gaan we even heel lelijk alles bij langs
        for i in range(0,len(levels)):
                                        # pak het hele lijstje aan dingen min 1tje, als het daarbij werkt kan je het goedkeuren
            levelsNew = [x for j,x in enumerate(levels) if j!=i]
            creasity = (levelsNew[1]-levelsNew[0])
            if creasity == 0:
                safe = False
            else:
                creasity /= abs(creasity)
                safe = not any([1 for j in range(0,len(levelsNew)-1) if not (1 <= creasity*(levelsNew[j+1]-levelsNew[j]) <= 3)])
            if safe:
                break                   # er is een veilig optie gevonden, prima kunnen we er dus gewoon uit
            elif i == len(levels)-1:
                safeness2 -= 1          # er is geen veilige optie gevonden :(

# printstatements for checking
# print(inputstring)
# print(input)

print("Number of safe reports in case 1: " + str(safeness1))
print("Number of safe reports in case 2: " + str(safeness2))