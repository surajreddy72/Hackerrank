def evenfib(n):
    list = []
    sum = 0
    list.append(1)
    while list[-1] < n:
        k = len(list)
        list.append(list[k-1]+list[k-2])
    if list[-1] > n:
        list.pop()
    for i in list:
        if i % 2 == 0:
            sum = sum + i
    print(sum)


inputs = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    inputs.append(n)
for i in inputs:
    evenfib(i)
