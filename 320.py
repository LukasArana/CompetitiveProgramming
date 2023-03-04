


s = input()
s = s + "11"
idx = 0
res = True
while (idx < len(s) and res):
    if (idx ==0 and s[idx] != "1"):
        res = False
    if(s[idx] == "4"  and s[idx:idx+3] == "444"):
        res = False
    if(s[idx] != "4" and s[idx] != "1"):
        res = False
    idx += 1
if (res):
    print("YES")
else:
    print("NO")
