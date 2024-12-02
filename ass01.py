# assignment 1

# uitlezen text bestandje
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()

# ID_left ID_right

ID_left = []
ID_right = []
for lines in input:                     # splitten op spaties en zetten in de losse waardes
    line = [int(x) for x in lines.split(" ") if x]
    ID_left.append(line[0])
    ID_right.append(line[1])

# oplossing voor 1
ID_left_sorted = sorted(ID_left)        # sorteren, dan is makkelijk
ID_right_sorted = sorted(ID_right)
distance = 0
for i in range(0,len(ID_left_sorted)):  # gewoon steeds het verschil pakken en toevoegen
    distance += abs(ID_left_sorted[i] - ID_right_sorted[i])

similarity = 0
# oplossing voor 2
for i in range(0, len(ID_left)):        # unit keer het aantal keer dat hij in de andere komt is mooi
    similarity += ID_left[i]*ID_right.count(ID_left[i])

# printstatements for checking
# print(inputstring)
# print(input)

print("The total distance is " + str(distance))
print("The total similarity is " + str(similarity))