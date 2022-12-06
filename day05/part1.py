import os
import re

dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
# input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

def moveCrates(stacks, number, start, end):
    for _ in range(number):
        stacks[end].append(stacks[start].pop())



rows = []

for lineNumber, line in enumerate(input):
    if line == "": break
    # match all alphanumeric characters and groups of three spaces
    rows.append(re.findall(r"(\w|    )", line))

numberOfStacks = int(rows.pop()[-1])
stacks = [[] for _ in range(numberOfStacks)]

while len(rows) > 0:
    row = rows.pop()
    for idx, elem in enumerate(row):
        if elem != "    ":
            stacks[idx].append(elem)

print(stacks)

for lineNumber in range((lineNumber + 1),len(input)):
    rawRow = input[lineNumber]
    instruction = re.findall(r'(\d+)', rawRow)

    number = int(instruction[0])
    start = int(instruction[1]) - 1
    end = int(instruction[2]) - 1

    moveCrates(stacks, number, start, end)

topCrates = ""

for stack in stacks:
    topCrates += stack[-1]

print(topCrates)
# SVFDLGLWV *