# 소수&팰린드롬
import math
n = int(input())
a = [0] * 10000001

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a)) + 1)):
    if a[i] == 0:
        continue
    for j in range(i + i, len(a), i):
        a[j] = 0

def isPalindrome(t):
    temp = list(str(t))
    s = 0
    e = len(temp) - 1
    while s < e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = n

while True:
    if a[i] != 0:
        result = a[i]
        if isPalindrome(result):
            print(result)
            break
    i += 1
