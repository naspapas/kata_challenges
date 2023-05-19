import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sortedArray = sorted(arr)
    lowestAddition = sortedArray[0] + sortedArray[1] + sortedArray[2] + sortedArray[3]
    highestAddition = sortedArray[1] + sortedArray[2] + sortedArray[3] + sortedArray[4]
    print (str(lowestAddition) + " " + str(highestAddition))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
