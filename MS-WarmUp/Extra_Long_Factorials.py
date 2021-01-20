#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = 1
    for num in range(2, n + 1):
        factorial *= num
    print(factorial)
    
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
