# assignment 5
import time

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# kijk mij eens goed list comprehension gebruiken :)
rules =     [(lines.split("|")[0],lines.split("|")[1]) for lines in input if "|" in lines]
orders =    [lines.split(",") for lines in input if "," in lines]

# part 1 (en het lijstje van deel 2 ophalen)
middlesum1 = 0
failedOrders = []
for order in orders:
    fail = False
    for i in range(0,len(order)-1):
        # mentionsL = [index for (index,item) in enumerate(rules) if item[0]==order[i]]
        mentionsR = [index for (index,item) in enumerate(rules) if item[1]==order[i]]
        for j in range(i+1,len(order)):
            if any([1 for index in mentionsR if rules[index][0] == order[j]]):
                failedOrders.append(order)
                fail = True
                break
        if fail:
            break
        elif i == len(order)-2:
            middlesum1 += int(order[int((len(order))/2)])

start = time.time()
# part 2
middlesum2 = 0
for order in failedOrders: # its bubblesorting time, maar net niet helemaal
    for n in range(len(order) -1, 0, -1):
        swap = False
        # hier doen we praktisch hetzelfde als zonet, maar wisselen we ze als het fout gaat
        # ook doe ik niet het echte bubblesort met dat je steeds overnieuw gaat, want dat heeft geen zin met deze willekeurige sorteerregels
        for i in range(n):
            # mentionsL = [index for (index,item) in enumerate(rules) if item[0]==order[i]]
            mentionsR = [index for (index,item) in enumerate(rules) if item[1]==order[i]]
            for j in range(i+1,len(order)):
                if any([1 for index in mentionsR if rules[index][0] == order[j]]):
                    order[j],order[i] = order[i],order[j]
                    swap = True
        if not swap:
            middlesum2 += int(order[int((len(order))/2)])
            break
print(str(time.time()-start))

# printstatements for checking
# print(inputstring)
# print(input)

# print(rules)
# print(orders)

print(middlesum1)
print(middlesum2)