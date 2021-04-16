# binpack.py
# name: Kimberly Tom
# CS325 Homework 8

import sys
import os

# create a Bin class
# https://www.w3schools.com/python/python_classes.asp
class Bin:
        # creating a new bin
        def __init__(self, capacity):
            self.capacity = capacity
        # setting capacity
        def createCapacity(self, capacity):
            self.capacity = capacity

# put each item as you come to it into the first (earliest opened) bin into which it fits
# if there is no available bin then open a new bin
# https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
def firstFitAlgorithm(numItems, binCapacity, itemWeights):
    # numberOfBins holds the total number of bins we are using, start with 1 bin
    numberOfBins = 1

    # create an array totalBins to hold all the bins we are using
    totalBins = []

    # create a bin with max capacity
    makeBin = Bin(binCapacity)

    # add the created bin to totalBins array
    totalBins.append(makeBin)

    # place items into the bins
    for i in range(numItems):
        itemStored = 0

        # go through the bins
        for b in range(numberOfBins):
            # if item can fit into a bin we already created, store in that bin
            if itemWeights[i] <= totalBins[b].capacity:
                totalBins[b].capacity = totalBins[b].capacity - itemWeights[i]
                itemStored = 1
                break
         # if not, store in a new bin
        if not itemStored:
            newBinCapacity = binCapacity - itemWeights[i]
            makeBin = Bin(newBinCapacity)
            totalBins.append(makeBin)
            numberOfBins = numberOfBins + 1

    return numberOfBins



# first sort the items in decreasing order by size, then use First-Fit on the resulting list
def decreasingAlgorithm(numItems, binCapacity, itemWeights):
    # make a copy of the array itemWEights
    decreasingWeights = itemWeights.copy()

    # sort the array decreasingWeights from greatest to least weight
    # https://www.geeksforgeeks.org/python-list-sort/
    decreasingWeights.sort(reverse = True)

    # call firstFitAlgorithm function and store in number of bins then return the number of bins
    numberOfBins = firstFitAlgorithm(numItems, binCapacity, decreasingWeights)

    return numberOfBins

# Place the items in order in which they arrive. Place next item into bin which will leave the least room
# left over after the item is placed in the bin.  If it doesn't fit in any bin, start new bin
def bestFitAlgorithm(numItems, binCapacity, itemWeights):
    # numberOfBins holds the total number of bins we are using, start with 1 bin
    numberOfBins = 1

    # create an array totalBins to hold all the bins we are using
    totalBins = []

    # create a bin with max capacity
    makeBin = Bin(binCapacity)

    # add the created bin to totalBins array
    totalBins.append(makeBin)

    # place items into the bins
    for i in range(numItems):
        tempStore = -1
        leastRoomLeftOver = binCapacity
        currentBinRoomLeftOver = 0

        # go through the bins
        for b in range(numberOfBins):
            # if item can fit into a bin we already created, potentially store in that bin
            if itemWeights[i] <= totalBins[b].capacity:
                currentBinRoomLeftOver = totalBins[b].capacity - itemWeights[i]
                # if the current bin has less room left over than the prior least room left over bin, update temp bin
                if currentBinRoomLeftOver < leastRoomLeftOver:
                    leastRoomLeftOver = currentBinRoomLeftOver
                    tempStore = totalBins[b]
        # place the item in the bin with the least amount of room leftover
        if tempStore != -1:
            tempStore.capacity = tempStore.capacity - itemWeights[i]
        # if no bin has enough room, store in a new bin
        else:
            newBinCapacity = binCapacity - itemWeights[i]
            makeBin = Bin(newBinCapacity)
            totalBins.append(makeBin)
            numberOfBins = numberOfBins + 1



    return numberOfBins

def main():
    # open a file for reading
    data_file = open("bin.txt", "r")


    array = []
    currentCase = 0

    # for each line in the data file
    for line in data_file:
        array.extend(line.split())

    array = list(map(int,array))
    testCaseCount = array.pop(0)

    # for each case in the number of test cases
    for t in range(testCaseCount):
        # store each bin's capacity
        binCapacity = 0
        # store the number of items in a test case
        numItems = 0
        # array to store the items' weights for a test case
        itemWeights = []

        # read number from file and store in binCapacity and numItems
        binCapacity = array.pop(0)
        numItems = array.pop(0)

        # for each item in the number of items
        for i in range(numItems):
            # store item weights in the itemWeights array
            itemWeights.append(array.pop(0))

        # print results
        print("\nTest Case #", currentCase + 1)
        currentCase += 1
        print(" First Fit: ", firstFitAlgorithm(numItems, binCapacity, itemWeights))
        print(" First Fit Decreasing: ", decreasingAlgorithm(numItems, binCapacity, itemWeights))
        print(" Best Fit: ", bestFitAlgorithm(numItems, binCapacity, itemWeights))


    data_file.close()

# call main function to start program
if __name__ == '__main__':
    main()