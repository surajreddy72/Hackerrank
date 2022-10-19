import math


def bPrime(n):
    while True:
        p = sPrime(n)
        if p < n:
            n //= p
        else:
            return str(n)


def sPrime(n):
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
    print(bPrime(i))


