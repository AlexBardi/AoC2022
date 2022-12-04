import os

def priority(letter):
    asciiNum = ord(letter)

    if asciiNum < 97: return asciiNum - 38 # asciiNum - 65 + 27
    return asciiNum - 96

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")

totalPriority = 0

for idx in range(len(input) // 3):
    rucksack1 = set([char for char in input[(idx * 3)]])
    rucksack2 = set([char for char in input[(idx * 3) + 1]])
    rucksack3 = set([char for char in input[(idx * 3) + 2]])
    commonLetter = list(rucksack1.intersection(rucksack2.intersection(rucksack3)))[0]
    totalPriority += priority(commonLetter)

# 2518
print(totalPriority)
