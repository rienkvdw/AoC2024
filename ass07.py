# assignment 7
import re
import time

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    calibrations = [list(map(int,re.split(r'[: ]+', line))) for line in input]

# wait we use functions now? Poggies
def addimultibad(calibra, n, perm, locsum): # iets met of de rekenmachine wel rekening houd met de order of operation
    if n <= len(calibra)-2:
        if perm[len(perm)-n] == 0:          # add
            return addimultibad(calibra,n+1,perm, locsum+calibra[n+1])
        elif perm[len(perm)-n] == 1:        # multiply 
            return addimultibad(calibra,n+1,perm, locsum*calibra[n+1])
        else:                               # concatenate
            return addimultibad(calibra,n+1,perm, int(str(locsum) + str(calibra[n+1])))
    else:
        return locsum
    
# part 1
ts = time.time()
total1 = 0
options = 2
for n in range(len(calibrations)):
    for i in range(pow(options,(len(calibrations[n])-2))):
        # splitsen in 0 (add) en 1 (multiply), zou in binary kunnen maar nu werkt het ook met deel 2 
        permutations = [int(i/pow(options,x)%options) for x in range(len(calibrations[n])-2)]
        currentsum = addimultibad(calibrations[n],1,permutations,calibrations[n][1])
        if currentsum == calibrations[n][0]:
            total1 += calibrations[n][0]
            break
print("Deel 1 kostte " + str(time.time()-ts))

# part 2
ts = time.time()
total2 = 0
options = 3
for n in range(len(calibrations)):
    for i in range(pow(options,(len(calibrations[n])-2))):
        # splitsen in 0 (add), 1 (multiply) en 2 (concatenate)
        permutations = [int(i/pow(options,x)%options) for x in range(len(calibrations[n])-2)]
        currentsum = addimultibad(calibrations[n],1,permutations,calibrations[n][1])
        if currentsum == calibrations[n][0]:
            total2 += calibrations[n][0]
            break
print("Deel 2 kostte " + str(time.time()-ts))

# printstatements for checking
# print(input)

# print(calibrations)

print("The total for part one is " + str(total1))
print("The total for part two is " + str(total2))