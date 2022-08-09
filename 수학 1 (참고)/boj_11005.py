# 진법 변환 2
import sys

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, sys.stdin.readline().split())
ans = ''

while n != 0:
    ans += str(system[n % b])
    n = n // b

print(ans[::-1])b 