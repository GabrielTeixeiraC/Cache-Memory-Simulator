import sys
import math

def printCache(validBits, addresses):
    size = len(addresses)
    print("=" * 16)
    print("IDX V ** ADDR **")
    for i in range(size):
        if addresses[i] == -1:
            print(str(i).zfill(3), validBits[i])
        else:
            print(str(i).zfill(3), validBits[i], addresses[i])

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
    if (address == ''):
        continue
    number = int(address, 16)
    binaryNumber = bin(number)[2:].zfill(32)

    index = binaryNumber[:indexSize].zfill(32)
    offset = binaryNumber[-offsetSize:]
    tag = binaryNumber[indexSize:-offsetSize].zfill(32)
    hexIndex = '0x' + hex(int(index, 2))[2:].zfill(8).upper()

    position = int(tag, 2) % numberOfGroups

    LRUIndex = 0
    swapped = False

    for i in range(groupSize):
        line = position * groupSize + i
        if validBits[line] == 0:
            validBits[line] = 1
            addresses[line] = hexIndex
            swapped = True
            timestamps[line] = 0
            break
        else:
            if addresses[line] == hexIndex:
                timestamps[line] = 0
                swapped = True
                break
            else:
                LRUIndex = max(LRUIndex, i)
    if (not swapped):
        addresses[LRUIndex] = hexIndex
        timestamps[LRUIndex] = 0    

    printCache(validBits, addresses)
