n = input()
k = []
for x in n:
    if x not in k:
        k.append(x)
if(len(k) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
