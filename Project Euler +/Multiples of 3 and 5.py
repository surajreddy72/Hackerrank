#100 points for this 

t = int(input())
list = []
for _ in range(t):
    n = input()
    list.append(n)
for j in list:
    sum = 0
    i = int(j)-1
    n1 = int(i)//3
    n2 = int(i)//5
    n3 = int(i)//15
    sum = (3*n1*(n1+1)//2) + (5*n2*(n2+1)//2) - (15*n3*(n3+1)//2)
    print(int(sum))


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
# Since time complexity is more
