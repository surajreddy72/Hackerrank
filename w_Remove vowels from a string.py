a=input()
output=[]
for i in a:
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        output.append(i)
for i in output:
    print(i,end='')
