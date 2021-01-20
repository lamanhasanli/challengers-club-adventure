#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    best_record = 0
    worst_record = 0

    for i in range(len(scores)):
        if scores[i] > highest:
            highest = scores[i]
            best_record += 1
            
        if scores[i] < lowest:
            lowest = scores[i]
            worst_record += 1
            
    return best_record, worst_record

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
