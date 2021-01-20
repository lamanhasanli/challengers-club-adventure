#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    row = math.floor(math.sqrt(len(s)))
    column = math.ceil(math.sqrt(len(s)))
    encrypted = ""
    
    for i in range(column):
        encrypted += s[i::column]
        encrypted += " "
        
    return encrypted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
