# Base Conversion
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))[::-1]
ten = 0

for i in range(m):
    ten += arr[i] * (a ** i)

result = []
while ten != 0:
    result.append(ten % b)
    ten //= b

print(" ".join(map(str, result[::-1])))
