#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    total = 0
    for i in n:
        total += int(i)
    total = total * k    
    
    super_digit = 0
    for i in str(total):
        super_digit += int(i)    
    if super_digit < 10:
        return super_digit
    
    return superDigit(str(super_digit), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
