# 연속합 2
n = int(input())
a = list(map(int, input().split()))
d = [[0] * n for _ in range(2)]
d[0][0] = a[0]
d[1][0] = -1000

for i in range(1, n):
    d[0][i] = max(d[0][i-1] + a[i], a[i])
    d[1][i] = max(d[0][i-1], d[1][i-1] + a[i])

print(max(max(d[0]), max(d[1])))