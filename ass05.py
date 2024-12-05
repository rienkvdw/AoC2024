# assignment 5
# import numpy as np

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# kijk mij eens goed list comprehension gebruiken :)
rules =     [(lines.split("|")[0],lines.split("|")[1]) for lines in input if "|" in lines]
orders =    [lines.split(",") for lines in input if "," in lines]

# part 1
middlesum = 0
for order in orders:
    fail = False
    for i in range(0,len(order)-1):
        # mentionsL = [index for (index,item) in enumerate(rules) if item[0]==order[i]]
        mentionsR = [index for (index,item) in enumerate(rules) if item[1]==order[i]]
        for j in range(i+1,len(order)):
            if any([1 for index in mentionsR if rules[index][0] == order[j]]):
                fail = True
                break
        if fail:
            break
        elif i == len(order)-2:
            middlesum += int(order[int((len(order))/2)])

# part 2

# printstatements for checking
# print(inputstring)
# print(input)

print(rules)
print(orders)
print(middlesum)