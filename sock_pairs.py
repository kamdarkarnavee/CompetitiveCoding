#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if n <= 1:
        return 0
    sum = 0
    count = 1
    ar = sorted(ar)
    for i in range(n-1):
        if ar[i] == ar[i+1]:
            count += 1
        else:
            sum += int(count/2)
            count = 1
    sum += int(count/2)
    return sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
