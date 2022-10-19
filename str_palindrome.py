count = 0
for i in range(int(input())):
    m = input()
    n = m[::-1]
    if (m == n):
        count = count+len(m)
    else:
        continue
print(count)
