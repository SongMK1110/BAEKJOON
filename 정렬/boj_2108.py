# 통계학
import sys
from collections import Counter
n = int(sys.stdin.readline())

num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(num)/n))

# 중앙값
num.sort()
print(num[n//2])

# 최빈값
nums = Counter(num).most_common()
if len(nums) > 1:
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])
else:
    print(nums[0][0])

# 범위
print(max(num) - min(num))    