#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    print(s)
    if s[8] == "P":
        newint = s[0] + "" + s[1]
        convertedTime = int(newint + 12)
        print(convertedTime)
        

if __name__ == '__main__':
    s = "08:05:00PM"

