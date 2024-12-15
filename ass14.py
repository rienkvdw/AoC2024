# assignment 14
import time
import re
import numpy as np

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
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

class Robot:
    def __init__(self,values):
        self.pos = Coordinate(values[0:3])
        self.vel = Coordinate(values[2:4])
    def __str__(self):
        return str((self.pos,self.vel))
    def __repr__(self):
        return str((self.pos,self.vel))

# part 1
ts = time.time()
robots = []
for line in input:                                      # regular expression die ook negatieve getalletjes meeneemt
    robots.append(Robot([int(x) for x in re.findall(r'-?\d+',line)]))
size = (101,103)
tiles = np.zeros(size)
for robot in robots:                                    # we doen lekker 100 stapjes
    for t in range(100):
        robot.pos.x = (robot.pos.x + robot.vel.x + size[0])%size[0]
        robot.pos.y = (robot.pos.y + robot.vel.y + size[1])%size[1]
    tiles[robot.pos.x][robot.pos.y] += 1
quadrants = np.zeros(4)
for i in range(0,int((size[0]-1)/2)):                   # we loopen over wat elke quadrant heeft aan ding, want list comprehension wou niet werken
    for j in range(0,int((size[1]-1)/2)):
        quadrants[0] += tiles[i][j]
        quadrants[1] += tiles[i+int((size[0])/2)+1][j]
        quadrants[2] += tiles[i][j+int((size[1])/2)+1]
        quadrants[3] += tiles[i+int((size[0])/2)+1][j+int((size[1])/2)+1]
print("Deel 1 kostte " + str(time.time()-ts))           # 0.03s

# part 2
ts = time.time()
robots2 = []
for line in input:                                      # heb de posities verandert van de vorige, dus moet ff nieuwe lijstje maken
    robots2.append(Robot([int(x) for x in re.findall(r'-?\d+',line)]))
from statistics import variance                         # oh boy time for some math
for t in range(max(size[0],size[1])):                   # voor de dimensions van de langste kan je kijken naar de variance
    positionsx = []
    positionsy = []
    for robot in robots2:                               # we pakken de positie van alle botjes (en incrementen daarna voor volgende stap)
        positionsx.append(robot.pos.x)
        positionsy.append(robot.pos.y)
        robot.pos.x = (robot.pos.x + robot.vel.x + size[0])%size[0]
        robot.pos.y = (robot.pos.y + robot.vel.y + size[1])%size[1]
    if t == 0:                                          # initialize die positie
        varx = variance(positionsx)
        tx = 0
        vary = variance(positionsy)
        ty = 0
    else:                                               # laagste variance timestep is waar kerstboom vormt voor die dimensie
        if varx > variance(positionsx):
            varx = variance(positionsx)
            tx = t
        if vary > variance(positionsy):
            vary = variance(positionsy)
            ty = t
for n in range(size[1]):                                # dan moet je kijken wanneer dat overlapt, aangezien dimensies niet gelijk zijn gebeurt dat ergens
    for m in range(size[0]):
        if n*size[0]+tx == m*size[1]+ty:
            tboom = n*size[0]+tx
            break
    else:
        continue
    break
print("Deel 2 kostte " + str(time.time()-ts))           # 0.12s

# printstatements for checking
# print(input)
# print(robots)
# print(tiles)
# print(quadrants)

from functools import reduce
from operator import mul
print("The safety factor is " + str(int(reduce(mul,quadrants))))
print("Het is boom tijd om " + str(tboom))