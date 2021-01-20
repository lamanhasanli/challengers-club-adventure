#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    time = ''
    words = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    
    if m == 1:
        time = words[m] + ' minute past ' + words[h]
    elif m == 0:
        time = words[h] + " o' clock"
    elif m == 15:
        time = "quarter past " + words[h]
    elif m == 30:
        time = "half past " + words[h]
    elif m == 45:
        time = "quarter to " + words[h + 1]
    elif m < 20:
        time = words[m] + ' minutes past ' + words[h]
    elif m < 30:
        time = words[-1] + ' ' + words[int(m % 10)] + ' minutes past ' + words[h]
    elif m > 45:
        time = words[60 - m] + ' minutes to ' + words[h + 1]
    else:
        time = words[-1] + ' ' + words[int(m%10)] + ' minutes to ' + words[h + 1]
    
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
