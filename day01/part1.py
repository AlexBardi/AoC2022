
input = open("./input.txt").read().strip('\n\n').split("\n")

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
