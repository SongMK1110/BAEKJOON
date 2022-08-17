# 리모컨
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
error = list(map(int, input().split()))

min_cnt = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for i in range(len(nums)):
        if int(nums[i]) in error:
            break
        elif i == len(nums) - 1:
            min_cnt = min(min_cnt, abs(int(nums) - target) + len(nums))

print(min_cnt)