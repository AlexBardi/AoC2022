import os
import re

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
#input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

totalFullContainment = 0

for line in input:
    numbers = re.findall(r"[0-9]+", line)
    firstElfLowerBound = int(numbers[0]) 
    firstElfUpperBound = int(numbers[1]) 
    secondElfLowerBound = int(numbers[2])
    secondElfUpperBound = int(numbers[3])

    if firstElfLowerBound <= secondElfLowerBound and firstElfUpperBound >= secondElfUpperBound: 
        totalFullContainment +=1
    elif firstElfLowerBound >= secondElfLowerBound and firstElfUpperBound <= secondElfUpperBound: 
        totalFullContainment +=1 

print(totalFullContainment)

# 233 - didn't include the case where both ranges are equal
# 249 - included the above edge case wrong, I was using < and > but those wouldn't work if one 
#           bound was equal
# 516 - I didn't convert the bounds to ints, so the logical operations weren't sorting right,
#           ex: 18-48,8-14 
# 477 *