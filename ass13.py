# assignment 13
import time
import re

# uitlezen text bestandje
with open('inputtest.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# damn zelfs classes gaan gebruiken
class Coordinate:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self = (self.x,self.y)
    def __str__(self):
        return str((self.x,self.y))

# nog een class
class Machine:
    def __init__(self, lines):
        self.a = Coordinate([int(x) for x in re.findall(r'\d+',lines[0])])
        self.b = Coordinate([int(x) for x in re.findall(r'\d+',lines[1])])
        self.prize = Coordinate([int(x) for x in re.findall(r'\d+',lines[2])])
    def __str__(self):
        return str([(self.a.x,self.a.y), (self.b.x,self.b.y), (self.prize.x,self.prize.y)])
    def __repr__(self):
        return str([(self.a.x,self.a.y), (self.b.x,self.b.y), (self.prize.x,self.prize.y)])

# dit had geen functie hoeven zijn
def findMachines(input):
    machines = []
    for n in range(int(len(input)/4+1)):
        machines.append(Machine(input[n*4:n*4+3]))
    return machines

# part 1
ts = time.time()
machines = findMachines(input)
costs = []
for machine in machines:            
    cost = 0
    for i in range(0,100):
        for j in range(0,100):
            if  i*machine.a.x + j*machine.b.x == machine.prize.x and \
                i*machine.a.y + j*machine.b.y == machine.prize.y:
                cost = 3*i+j
                break
        else:
            continue
        break
    costs.append(cost)

print("Deel 1 kostte " + str(time.time()-ts))   # duurt ongeveer 0.6s

# part 2 dit is nog enorm traag, maar ik weet niet hoe ik het moet gaan doen
ts = time.time()
machines2 = machines
costs2 = []
for machine in machines2:
    machine.prize.x += 10000000000000
    machine.prize.y += 10000000000000
    # n = min(int(machine.prize.x/machine.b.x),int(machine.prize.y/machine.b.y))
    # for i in range(n,0,-1):
    #     if  (machine.prize.x - (i*machine.b.x)) % machine.a.x == 0 and \
    #         (machine.prize.y - (i*machine.b.y)) % machine.a.y == 0:
    #         costs2.append(int(i + 3*(machine.prize.x - (i*machine.b.x)) / machine.a.x))
    #         print(len(machines2)-len(costs2))
    #         break

print("Deel 2 kostte " + str(time.time()-ts))

# printstatements for checking
# print(input)
# print(machines)
# print(costs)

# print(machines2)

print(costs)

print("The total cost for part 1 is " + str(sum(costs)))
print("The total cost for part 2 is " + str(sum(costs2)))