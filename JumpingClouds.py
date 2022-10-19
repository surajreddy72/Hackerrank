#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while(i <= len(c)):
        if (i+2 < len(c) and c[i+2] == 1):
            jumps = jumps + 1;
            i = i+1;
        elif (i+2 < len(c) and c[i+2] == 0):
            jumps = jumps + 1;
            i = i+2;
        else:
            break;
    return(jumps)


if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
