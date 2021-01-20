#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    total_sum, min_sum, max_sum = 0, 0 ,0
    for i in arr:
        total_sum += i
        
    min_sum = total_sum - arr[-1]
    max_sum = total_sum - arr[0]
    
    print(min_sum, max_sum)
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
