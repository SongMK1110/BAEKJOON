# 행렬 덧셈
n, m = map(int, input().split())
a, b = [], []

for i in range(n):
    i = list(map(int, input().split()))
    a.append(i)

for j in range(n):
    j = list(map(int, input().split()))
    b.append(j)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()