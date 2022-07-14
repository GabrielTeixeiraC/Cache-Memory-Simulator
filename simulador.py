import sys
import math

def printCache(validBits, addresses):
    size = len(addresses)
    print("=" * 16)
    print("IDX V ** ADDR **")
    for i in range(size):
        pass

        

cacheSize = int(sys.argv[1])
cacheLineSize = int(sys.argv[2])
groupSize = int(sys.argv[3])
filename = sys.argv[4]

offsetSize = int(math.log(cacheLineSize, 2))

numberOfLines = cacheSize // cacheLineSize
numberOfGroups = numberOfLines // groupSize

tagSize = int(math.log(numberOfGroups, 2))

indexSize = 32 - tagSize - offsetSize

with open(filename, 'r') as file:
    fileContent = file.read().split('\n')

validBits = [0 for i in range(numberOfLines)]
addresses = [-1 for i in range(numberOfLines)]
timestamps = [0 for i in range(numberOfLines)]

for address in fileContent:
    number = int(address, 16)
    binaryNumber = bin(number)[2:].zfill(32)

    index = binaryNumber[:indexSize].zfill(32)
    offset = binaryNumber[-offsetSize:]
    tag = binaryNumber[indexSize:-offsetSize].zfill(32)
    hexIndex = '0x' + hex(int(index, 2))[2:].zfill(8).upper()

    position = int(tag, 2) % numberOfGroups

    LRUIndex = 0

    for i in range(groupSize):
        line = position * groupSize + i
        if validBits[line] == 0:
            validBits[line] = 1
            addresses[line] = hexIndex
            timestamps[line] = 0
            break
        else:
            if addresses[line] == hexIndex:
                timestamps[line] = 0
                break
            else:
                LRUIndex = max(LRUIndex, i)
    if (LRUIndex > 0):
        addresses[LRUIndex] = hexIndex
        timestamps[LRUIndex] = 0    

print()