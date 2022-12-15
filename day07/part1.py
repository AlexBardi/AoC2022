import os
import re

CD = "$ cd"
LS = "$ ls"

def main():
    dir_path = os.path.dirname(__file__)

    # Windows paths
    # input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")
    # input = open(dir_path + "\\test.txt").read().strip('\n\n').split("\n")

    # Unix file paths
    input = open(dir_path + "/input.txt").read().strip('\n\n').split("\n")
    # input = open(dir_path + "/test.txt").read().strip('\n\n').split("\n")

    lineIdx = 0
    dirToContents = {}
    childToParent = {}
    currDir = ""
    dirs = set()
    fileSizes = {}

    while lineIdx < len(input):
        currLine = input[lineIdx]
        if currLine[0:4] == CD:
            currDir = processCD(currLine, currDir, dirToContents, childToParent, fileSizes, dirs)
            lineIdx += 1
        elif currLine[0:4] == LS:
            lineIdx = processLS(lineIdx, currDir, input, dirToContents, childToParent, fileSizes)
        else:
            print("Error: line didn't match")
            print(currLine[0:3])
            return

    sizeUpDirs('/', fileSizes, dirToContents)

    totalSize = 0
    for dir in dirs:
        size = fileSizes[dir]
        if size <= 100000:
            totalSize += size

    print(totalSize)

def processCD(currLine, currDir, dirToContents, childToParent, fileSizes, dirs):
    arg = currLine[5:]
    if arg == "..":
        readyToSize = True
        for content in dirToContents:
            if (content not in fileSizes) or (fileSizes[content] == -1):
                readyToSize = False
                break
        if readyToSize: sizeUpDirs(currDir, fileSizes, dirToContents)
        return childToParent[currDir]
    else:
        dirs.add(arg)
    return arg
    

def processLS(lineIdx, currDir, input, dirToContents, childToParent, fileSizes):
    lineIdx += 1
    currLine = input[lineIdx]

    while currLine[0] != '$':
        # stuff
        if currLine[0:3] == "dir":
            name = currLine[4:]
            size = -1
        else:
            results = re.findall(r"(\S+)", currLine)
            name = results[1]
            size = int(results[0])

        if currDir in dirToContents:
            dirToContents[currDir].append(name)
        else:
            dirToContents[currDir] = [name]

        childToParent[name] = currDir
        fileSizes[name] = size

        lineIdx += 1
        if lineIdx == len(input):
            return lineIdx
        currLine = input[lineIdx]
    
    return lineIdx

def sizeUpDirs(dir, fileSizes, dirToContents):
    size = 0

    for content in dirToContents[dir]:
        if fileSizes[content] == -1:
            sizeUpDirs(content, fileSizes, dirToContents)
        size += fileSizes[content]

    fileSizes[dir] = size

if __name__=="__main__":
    main()