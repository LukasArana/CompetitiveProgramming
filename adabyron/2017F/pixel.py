


dic=  {"R": (1,1,0), "L":(1, 0, 1), "V":(0, 1, 1), "N": (1, 1, 1), "A":(0, 1, 0), "C": (0, 0, 1), "M": (1, 0, 0), "B": (0, 0, 0)}

n = int(input())
for i in range(n):
    l = input().split()
    dispo = list(map(int, l[:3]))
    color = str(l[3:])[2:-2]
    for i in color:
        dispo[0] += -dic[i][0]
        dispo[1] += -dic[i][1]
        dispo[2] += -dic[i][2]

    if (all( i >= 0 for i in dispo)):
        print("SI " + " ".join(map(str, dispo)))
    else:
        print("NO")
