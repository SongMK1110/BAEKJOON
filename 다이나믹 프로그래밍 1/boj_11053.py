# 가장 긴 증가하는 부분 수열
n = int(input())
a = list(map(int, input().split()))
d = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))