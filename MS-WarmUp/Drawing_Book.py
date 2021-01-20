#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    turning_from_left = n //2 - p //2
    turning_from_right = p // 2
    
    if turning_from_right > turning_from_left:
        return turning_from_left
    else:
        return turning_from_right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
