# 거의 소수 구하기
from cmath import sqrt
import math
a, b = map(int, input().split())
li = [0] * (10000001)

for i in range(2, len(li)):
    li[i] = i

for i in range(2, int(math.sqrt(len(li)) + 1)):
    if li[i] == 0:
        continue
    for j in range(i + i, len(li), i):
        li[j] = 0

cnt = 0

for i in range(2, 10000001):
    if li[i] != 0:
        temp = li[i]
        while li[i] <= b / temp:
            if li[i] >= a / temp:
                cnt += 1
            temp = temp * li[i]

print(cnt)