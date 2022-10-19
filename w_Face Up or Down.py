for i in range(int(input())):
    a,b=map(int,input().split())
    if b >= a//2 :
        print(a-b)
    else:
        print(b)