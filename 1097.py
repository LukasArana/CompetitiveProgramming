



table = input()
res = 0
hand = input().split()
for i in hand:
    if table[0] in i or table[1] in i:
        res = 1
        break

if (res == 1):
    print("YES")
else:
    print("NO")
