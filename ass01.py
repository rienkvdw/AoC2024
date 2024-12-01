# assignment 1
import numpy as np
import numbers

# uitlezen text bestandje
with open('input.txt') as inputfile:
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# ID_left ID_right

ID_left = []
ID_right = []
for lines in input:
    line = [int(x) for x in lines.split(" ") if x]
    ID_left.append(line[0])
    ID_right.append(line[1])

# oplossing voor 1
ID_left_sorted = sorted(ID_left)
ID_right_sorted = sorted(ID_right)
distance = 0
for i in range(0,len(ID_left_sorted)):
    distance += abs(ID_left_sorted[i] - ID_right_sorted[i])

similarity = 0
# oplossing voor 2
for i in range(0, len(ID_left)):
    similarity += ID_left[i]*ID_right.count(ID_left[i])

# printstatements for checking
# print(inputstring)
# print(input)

print("The total distance is " + str(distance))
print("The total similarity is " + str(similarity))