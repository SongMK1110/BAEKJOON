# 오등큰수
from collections import Counter
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = []

for i in range(n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)