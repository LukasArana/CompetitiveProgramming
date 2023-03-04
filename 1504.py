



n = int(input())
for _ in range(n):
    a = int(input())

    l = map(int, input().split())

    bakoiti = 0
    bikoiti = 0
    for i in l:
        if (i % 2  == 0):
            bikoiti += 1
        else:
            bakoiti += 1
    if (bikoiti == bakoiti):
        print("Yes")
    else:
        print("No")
