# 60 points for this 

t = int(input())
list = []
for _ in range(t):
    n=input()
    list.append(n)
for i in list:
    sum = 0
    a = 1
    while a < int(i) :
        if a%3==0 or a%5==0 :
            sum = sum + a
        a = a + 1
    print(sum)
# Terminated due to timeout
