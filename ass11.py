# assignment 10
import time

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    stones = list(map(int,input[0].split()))

def blink(stones, operations):
    new_stones = []
    for stone in stones:
        if stone not in operations:
            if not stone:
                operations[stone] = [int(1)]
            else:
                digits = len(str(stone))
                if digits%2 == 0:
                    stone1 = int(stone // 10**(int(digits)/2))
                    stone2 = int(stone %  10**(int(digits/2)))
                    operations[stone] = [stone1,stone2]
                else:
                    operations[stone] = [stone*2024]
        new_stones.extend(operations[stone])
    return new_stones, operations

# part 1
ts = time.time()
blinks1 = 25
operations = {}
new_stones,operations = blink(stones,operations)
for n in range(blinks1-1):
    new_stones, operations = blink(new_stones,operations)
print("Deel 1 kostte " + str(time.time()-ts))       # duurt 0.04s
new_stones_25 = new_stones.copy()

# part 2
ts = time.time()
blinks2 = 40
# tb = time.time()
for n in range(blinks1-1, blinks2-1):
    # print("Blink number " + str(n) + ", previous blink cost " + str(time.time()-tb))
    # tb = time.time()
    new_stones, operations = blink(new_stones,operations)
print("Deel 2 kostte " + str(time.time()-ts))       # duurt 20s vior blink 40, dus voor 75 gaat het te lang duren

# printstatements for checking
# print(stones)

print("The total amount of stones after " + str(blinks1) + " blinks is " + str(int(len(new_stones_25))))
print("The total amount of stones after " + str(blinks2) + " blinks is " + str(int(len(new_stones))))