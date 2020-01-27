#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    l = len(c)
    i = 0
    count = 0
    while i < l:
        if i+2 < l and c[i+2] == 0:
            count += 1
            i += 1
        elif i+1 < l and c[i+1] == 0:
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
