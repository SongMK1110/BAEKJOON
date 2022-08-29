# 이항 계수 1
from math import factorial
n, k = map(int, input().split())

print(factorial(n) // (factorial(k) * factorial(n-k)))