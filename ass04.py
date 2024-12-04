# assignment 4
import numpy as np

# uitlezen text bestandje
wordsearch = []
with open('input.txt') as inputfile:    # input lezen en splitten in lines
    inputstring = inputfile.read()
    input = inputstring.splitlines()
    for lines in input:
        wordsearch.append([x for x in lines ])
wordsearch = np.pad(wordsearch,((1,1),(1,1)))

# part 1 fucking lelijke for tree
words = 0
for ix in range(0,len(wordsearch)):
    for jx in range(0, len(wordsearch[ix])):
        if wordsearch[ix][jx] == "X":
            # print("X found at (" + str(ix) + "," + str(jx) + ")")
            for im in range(ix-1,ix+2):
                for jm in range(jx-1,jx+2):
                    if wordsearch[im][jm] == "M":
                        # print("M found at (" + str(im) + "," + str(jm) + ")")
                        if wordsearch[ix-2*(ix-im)][jx-2*(jx-jm)] == "A":
                            # print("A found at (" + str(ix-2*(ix-im)) + "," + str(jx-2*(jx-jm)) + ")")
                            if wordsearch[ix-3*(ix-im)][jx-3*(jx-jm)] == "S":
                                # print("S found at (" + str(ix-3*(ix-im)) + "," + str(jx-3*(jx-jm)) + ")")
                                words += 1

# part 2 zelfde soort lelijke for tree
Xs = 0
for ia in range(0,len(wordsearch)):
    for ja in range(0, len(wordsearch[ia])):
        if wordsearch[ia][ja] == "A":
            # print("A found at (" + str(ia) + "," + str(ja) + ")")
            for im in range(ia-1,ia+2,2):
                for jm in range(ja-1,ja+2,2):
                    if wordsearch[im][jm] == "M":
                        # print("M found at (" + str(im) + "," + str(jm) + ")")
                        if wordsearch[2*ia-im][2*ja-jm] == "S":
                            # print("S found at (" + str(2*ia-im) + "," + str(2*ja-jm) + ")")
                            if wordsearch[2*ia-im][jm] == "M":
                                # print("M found at (" + str(2*ia-im) + "," + str(jm) + ")")
                                if wordsearch[im][2*ja-jm] == "S":
                                    # print("S found at (" + str(ia) + "," + str(2*ja-jm) + ")")
                                    Xs += 1
                                    break                           # gewone break
                            elif wordsearch[im][2*ja-jm] == "M":
                                if wordsearch[2*ia-im][jm] == "S":
                                    Xs += 1
                                    break                           # gewone break
                else:                   
                    continue                                        # om uit dubbele nested loop te komen, lelijk maar vond ik op stackovervlow
                break

# printstatements for checking
# print(inputstring)
# print(input)

print(wordsearch)
print(words)
print(Xs)