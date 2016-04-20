################################################
# Chapter 2 - Recursion and Backtracking
# "Data Structures and Algorithmic Thinking
# with Python" by Narasimha Karumanchi
# see readme
################################################


# Tower of Hanoi p.44
def towersHanoi(numDisks, startPeg=1, endPeg=3):
    if numDisks:
        towersHanoi(numDisks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (numDisks, startPeg, endPeg)
        towersHanoi(numDisks-1, 6-startPeg-endPeg, endPeg)
        
        
# Check if array is sorted p.45
def isSorted(array):
    # base case
    if len(array) == 1:
        return True
    return array[0] <= array[1] and isSorted(array[1:])


# Sorted check modified to return false if not sorted
def isSorted(array):
    if len(array) == 1:
        return True
    elif array[0] <= array[1]:
        return isSorted(array[1:])
    else:
        return False

    
# Time Complexity: O(n)
# Space Complexity: O(n) for recursive stack space