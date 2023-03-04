from time import sleep
n = int(input())

for i in range(n):
    _ = input()
    s = input()
    idx = 1
    s = "A" + s + "A"
    s= list(s)
    pintado = False
    while "?" in s:
        if(s[idx] == "?" and (s[idx+1] == "R" or s[idx-1] == "R")):
            s[idx] = "B"
            pintado = True
        elif (s[idx] == "?" and (s[idx +1] == "B" or s[idx -1] =="B")):
            s[idx] = "R"
            pintado = True

        idx += 1
        if (idx == (len(s) -1)):
            if not pintado and ("?" in s):
                for i in range(len(s)):
                    if (s[i] == "?"):
                        s[i] = "B"
                        break
            pintado = False
            idx = 1

    s = "".join(s)
    print(s[1:-1])
