# assignment 9
import time
import copy
import numpy as np

# uitlezen text bestandje
with open('inputtest.txt') as inputfile:    # input lezen en splitten in lines
    input = list(map(int,inputfile.read()))

# part 1
ts = time.time()
disk = []
for n in range(int(len(input)/2)):          # unitje maken
    disk.extend([n]*input[2*n])
    disk.extend(["."]*input[2*n+1])
if len(input) % 2 == 1:
    disk.extend([int(len(input)/2)]*input[len(input)-1])

IDs_r = [x for x in disk if isinstance(x,int)]
IDs_r.reverse()

disk_compact1 = []
m = 0
for n in range(len(disk)):
    if not isinstance(disk[n],int):         # als puntje, gooi dan maar de laatste van de vorige erin
        disk_compact1.append(IDs_r[m])
        m += 1
    else:                                   # anders het normale getal erin gooien
        disk_compact1.append(disk[n])
        if disk_compact1[n] == IDs_r[m]:    # als het getal dat toegevoegd is hetzelfde is als het volgende getal uit de queue
                                            # dan even het aantal dat daar nog van mist ook nog even toevoegen
            disk_compact1.extend([IDs_r[m] for x in range(n+1,n+1+input[IDs_r[m]*2]-disk_compact1.count(IDs_r[m]))])
            break

checksum1 = sum([n*disk_compact1[n] for n in range(len(disk_compact1))])
print("Deel 1 kostte " + str(time.time()-ts))

# part 2 doet het nog niet
ts = time.time()
# input_copy = input.copy()
# disk_compact2 = disk.copy()
# n  = 0
# while n < int(len(input_copy)/2):
#     for m in range(int(len(input_copy)/2),0,-1):
#         if input_copy[n*2+1] >= input_copy[m*2] and input_copy[m*2] != 0:
#             print(str(input_copy[n*2+1]) + " " + str(input_copy[m*2]))
#             input_copy[n*2+1] = input_copy[n*2+1]-input_copy[m*2]
#             input_copy[m*2] = 0
#             print(input_copy[n*2+1])
#             n -= 1
#             break
#     n += 1

# print(input_copy)
print("Deel 2 kostte " + str(time.time()-ts))

# printstatements for checking
# print(input)

# print(disk)
# print(disk_compact1)

print("The checksum for part one is " + str(checksum1))