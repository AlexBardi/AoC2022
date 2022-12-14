import os

def priority(letter):
    asciiNum = ord(letter)

    if asciiNum < 97: return asciiNum - 38 # asciiNum - 65 + 27
    return asciiNum - 96

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")

totalPriority = 0

for line in input:
    compartment1 = set([char for char in line[0:(len(line)//2)]])
    compartment2 = set([char for char in line[(len(line)//2):]])
    commonLetter = list(compartment1.intersection(compartment2))[0]
    totalPriority += priority(commonLetter)

print(totalPriority)

# 8018 *