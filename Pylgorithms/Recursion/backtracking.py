################################################
# Chapter 2 - Recursion and Backtracking
# "Data Structures and Algorithmic Thinking
# with Python" by Narasimha Karumanchi
# see readme
################################################


# n-bit string combinations p.45
def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    return [digit+bitstring for digit in bitStrings(1) 
                for bitstring in bitStrings(n-1)]
        
        
# string combinations length n from 0...k-1 p.46
def createArray(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result

def baseKStrings(n,k):
    if n == 0: return []
    if n == 1: return createArray(k)
    return [digit+bitstring for digit in baseKStrings(1,k) 
                for bitstring in baseKStrings(n-1,k)]


########################################################
# WARNING!!
# get length of largest connected cells of ones (regions) 
# in a matrix of zeros and ones p.46 
# this one appears to be incorrect in the book
# I will try to fix it soon  
# WARNING!!
def getCellVal(array, row, column, rowMax, columnMax):
    if ((row < 0) or (row >= rowMax) or (column < 0) or (column >= columnMax)):
        return 0
    else:
        return array[row][column]

def findMaxBlock(array, row, column, rowMax, columnMax, size):
    global maxSize
    global cntarr
    if ((row >= rowMax) or (column >= columnMax)):
        return
    cntarr[row][column] = 1
    size += 1
    if (size > maxSize):
        maxSize = size
    # search in eight directions
    direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    for i in range(0,7):
        newRow = row + direction[i][0]
        newColumn = column + direction[i][1]
        val = getCellVal(array, newRow, newColumn, rowMax, columnMax)
        if ((val > 0) and (cntarr[newRow][newColumn] == 0)):
            findMaxBlock(array, newRow, newColumn, rowMax, columnMax, size)
    cntarr[row][column] = 0

def findMaxRegion(array, rowMax, columnMax):
    global maxSize
    global size
    global cntarr
    for i in range(0, rowMax):
        for j in range(0, columnMax):
            if (array[i][j] == 1):
                findMaxBlock(array, i, j, rowMax, columnMax, size)
    return maxSize
    
