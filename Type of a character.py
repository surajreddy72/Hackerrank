a = ord(input())
if (a>=65 and a<=90):
    print("uppercase")
elif (a>=97 and a<=122):
    print("lowercase")
elif (a>=48 and a<=57):
    print("digit")
else:
    print(a)
