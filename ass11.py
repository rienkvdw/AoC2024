# assignment 11
import time
import math
from collections import defaultdict
import copy

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    # stones = list(map(int,input[0].split()))
    stones = defaultdict(int)
    for x in input[0].split():
        stones[x] += 1

def blinkDict(stones, operations):      # nieuwe (snelle?) implementatie met dict
    new_stones = defaultdict(int)
    for stonekey, stonevalue in stones.items():
        if stonekey not in operations:
            if int(stonekey) == 0:
                operations[stonekey] = int(1)
            else:
                digits = int(math.log10(int(stonekey))+1)   # log10 werkt mooi voor digits vinden
                if digits%2 == 0:
                    stone1 = int(int(stonekey) // 10**(int(digits)/2))
                    stone2 = int(int(stonekey) %  10**(int(digits/2)))
                    operations[stonekey] = [stone1,stone2]  # is list (kreeg geen andere goeie manier voor elkaar waarbij ik later niet hoef te checken)
                else:                                       # keer 2024
                    operations[stonekey] = int(stonekey)*2024
        if isinstance(operations[stonekey],list):           # ik doe niet helemaal slim, dus als er twee bij moeten is het edgecase
            new_stones[operations[stonekey][0]] += stonevalue
            new_stones[operations[stonekey][1]] += stonevalue
        else:
            new_stones[operations[stonekey]] += stonevalue
    return new_stones, operations

# part 1
ts = time.time()
blinks1 = 25
operations = {}
new_stones,operations = blinkDict(stones,operations)
for n in range(blinks1-1):
    new_stones, operations = blinkDict(new_stones,operations)

print("Deel 1 kostte " + str(time.time()-ts))       # duurt 7.6ms
new_stones_25 = copy.deepcopy(new_stones)

# part 2
ts = time.time()
blinks2 = 75
for n in range(blinks1-1, blinks2-1):
    new_stones, operations = blinkDict(new_stones,operations)
print("Deel 2 kostte " + str(time.time()-ts))       # duurt 96.5ms

# # printstatements for checking
# # print(stones)

print("The total amount of stones after " + str(blinks1) + " blinks is " + str(sum(new_stones_25.values())))
print("The total amount of stones after " + str(blinks2) + " blinks is " + str(sum(new_stones.values())))