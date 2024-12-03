# assignment 3
import re

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

data = []
for lines in input:                     # splitten op de gehele set waar ik voor wil checken
    y = re.split(r'[),]+', lines)       # met regular expression
    for x in y:
        data.extend(x.split("mul("))    # die ik net niet goed genoeg werkend kreeg voor mezelf waardoor ik dit extra nodig heb
    print(data)

# part 1
total1 = 0
for i in range(0,len(data)-1):          # als in mijn magische cursed data 2 values na elkaar alleen nummer zijn
                                        # dan mag het erbij
    if data[i].isnumeric() and data[i+1].isnumeric():
        total1 += int(data[i])*int(data[i+1])
        i += 1          

# part 2
total2 = 0
do = True
for i in range(0,len(data)-1):          # ik doe hetzelfde voor de tweede, maar check voor inputs of ze de magische woorden containen
    if do:
        if "don't(" not in data[i]:     # maar ik split eerder op ), dus ik check op het command zonder )
            if data[i].isnumeric() and data[i+1].isnumeric():
                total2 += int(data[i])*int(data[i+1])
                i += 1
        else:
            do = False
    else:
        if "do(" in data[i]:
            do = True

# printstatements for checking
# print(inputstring)
# print(input)

print("The total for part one is " + str(total1))
print("The total for part two is " + str(total2))