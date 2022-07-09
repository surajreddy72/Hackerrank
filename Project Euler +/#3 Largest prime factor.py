import math


def largestPrime(n):
    while True:
        p = Prime(n)
        if p < n:
            n //= p
        else:
            return str(n)


def Prime(n):
    n >= 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

inputs = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    inputs.append(n)
for i in inputs:
    print(largestPrime(i))
