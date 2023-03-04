n, m = map(int, input().split())
res = 0.0
for i in range(n):
    res += float(f"%.{m}f".format(1/(n^2), m))
print(res)
