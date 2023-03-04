


n = int(input())

m = [[1for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i != 0 and j != 0:
            m[i][j] = m[i-1][j] + m[i][j-1]
print( m[n-1][n-1])
