# 가장 긴 증가하는 부분 수열 4
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
arr = []
order = max(d)

for i in range(n-1, -1, -1):
    if d[i] == order:
        arr.append(a[i])
        order -= 1
arr.reverse()
print(*arr)
