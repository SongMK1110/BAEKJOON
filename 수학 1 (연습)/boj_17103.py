# 골드바흐 파티션
import sys

t = int(sys.stdin.readline())
nums = [int(input()) for _ in range(t)]
m = max(nums)

prime = [False, False] + [True] * (m-1)
for i in range(2, int(m**0.5) +1):
    if prime[i]:
        for j in range(i+i, m+1, i):
            if prime[j]:
                prime[j] = False

for i in nums:
    cnt = 0
    for j in range((i//2) +1):
        if prime[j] and prime[i-j]:
            cnt += 1
    
    print(cnt)
        