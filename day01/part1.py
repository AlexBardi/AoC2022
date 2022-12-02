import os

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
#input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

currCount = 0
maxCount = 0

for line in input:
    if line == '':
        if currCount > maxCount:
            maxCount = currCount
        currCount = 0
    else:
        currCount += int(line)

print(maxCount)

# 672393 Too high <- I wasn't clearing currCount when it wasn't overwriting maxCount
# 68775 *