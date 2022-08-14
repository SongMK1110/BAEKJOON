# 스티커
t = int(input())

for i in range(t):
    d = []
    n = int(input())
    for _ in range(2):
        d.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            d[0][j] += d[1][j-1]
            d[1][j] += d[0][j-1]
        else:
            d[0][j] += max(d[1][j-1], d[1][j-2])
            d[1][j] += max(d[0][j-1], d[0][j-2])
    
    print(max(d[0][n-1], d[1][n-1]))

