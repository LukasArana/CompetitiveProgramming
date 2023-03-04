n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    s = input()
    idx = 0
    while(idx < len(s)):
        if (x > 0 and s[idx] == "R"):
            x += -1
        elif(x < 0 and s[idx] == "L"):
            x += 1
        elif(y > 0 and s[idx] == "U"):
            y+= -1
        elif(y <0 and s[idx] == "D"):
            y+= 1
        idx += 1
    if (x ==0 and y ==0):
        print("YES")
    else:
        print("NO")
