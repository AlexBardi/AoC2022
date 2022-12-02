import os
import heapq

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
#input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

currCount = 0
sums = []

for line in input:
    if line == '':
        heapq.heappush(sums, currCount)
        currCount = 0
    else:
        currCount += int(line)

print(sum(heapq.nlargest(3, sums)))

# 202585 *