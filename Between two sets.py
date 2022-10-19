#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    ans = 0
    for i in range(a[-1], b[0]):
        if all(x % i == 0 for x in a) and all(i % x == 0 for x in b):
            ans = ans + 1
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = getTotalX(a, b)
    print(result)
