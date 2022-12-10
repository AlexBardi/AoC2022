import os

def incRange(endIdx, line, dict):
    removedIdx = endIdx - 13
    removedChar = line[removedIdx]
    addedIdx = endIdx + 1
    addedChar = line[addedIdx]
    print(removedChar, addedChar)

    # Sanity check, this should always be true
    if removedChar in dict:
        if dict[removedChar] > 1:
            dict[removedChar] -= 1
        else:
            del dict[removedChar]
    else:
        print("Uhh, why did we try to remove a char that isn't in the dictionary?")
        print(endIdx, line, dict)

    if addedChar in dict:
        dict[addedChar] += 1
    else:
        dict[addedChar] = 1

    return

dir_path = os.path.dirname(__file__)

# input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
# input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

input = open(dir_path + "/input.txt").read().strip('\n\n').split("\n")
# input = open(dir_path + "/test.txt").read().strip('\n\n').split("\n")

solns = []

for line in input:
    print(line)
    #init first rectangle
    dict = {}

    for idx in range(14):
        char = line[idx]
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    endIdx = 13
    if len(dict) == 14:
        # solns aren't zero indexed
        solns.append(endIdx + 1)
        continue

    while len(dict) < 14:
        incRange(endIdx, line, dict)
        endIdx += 1

    solns.append(endIdx + 1)


print(solns)
# 1887 - forgot to change the init value of endIdx
# 2635 *