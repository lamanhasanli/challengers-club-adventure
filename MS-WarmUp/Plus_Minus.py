#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zeros = 0, 0, 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zeros += 1
            
    print(round(positive/ len(arr), 6))
    print(round(negative/ len(arr), 6))
    print(round(zeros/ len(arr), 6))
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
