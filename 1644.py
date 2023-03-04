

n = int(input())
for i in range(n):
    s = input()
    b = False
    r = False
    g = False
    p = True
    for j in s:
        if (j.islower()):
            if (j == "b"):
                b = True
            elif(j =="r"):
                r = True
            else:
                g = True
        else:
            if ((j == "B" and not b) or(j == "R" and not r )or (j == "G" and not g)):
                 p = False
                 break

    if p:
        print("YES")
    else:
        print("NO")
