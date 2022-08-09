# 진법 변환
import sys

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = sys.stdin.readline().split()
b = int(b)
ans = 0
n = n[::-1]

for i in range(len(n)):
    ans += system.index(n[i]) * (b ** i)

print(ans)
