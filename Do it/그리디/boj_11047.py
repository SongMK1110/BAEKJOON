# 동전 개수의 최솟값 구하기
n, k = map(int, input().split())
a = [0] * n

for i in range(n):
    a[i] = int(input())

cnt = 0

for i in range(n-1, -1, -1):
    if a[i] <= k:
        cnt += int(k / a[i])
        k = k % a[i]

print(cnt)