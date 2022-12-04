import os
import re

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
#input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

totalOverlap = 0

for line in input:
    numbers = re.findall(r"[0-9]+", line)
    firstElfLowerBound = int(numbers[0]) 
    firstElfUpperBound = int(numbers[1]) 
    secondElfLowerBound = int(numbers[2])
    secondElfUpperBound = int(numbers[3])

    if firstElfLowerBound >= secondElfLowerBound and firstElfLowerBound <= secondElfUpperBound: 
        totalOverlap +=1
    elif firstElfUpperBound >= secondElfLowerBound and firstElfUpperBound <= secondElfUpperBound: 
        totalOverlap +=1
    elif secondElfLowerBound >= firstElfLowerBound and secondElfLowerBound <= firstElfUpperBound:
        totalOverlap += 1
    elif secondElfUpperBound >= firstElfLowerBound and secondElfUpperBound <= firstElfUpperBound:
        totalOverlap += 1

print(totalOverlap)