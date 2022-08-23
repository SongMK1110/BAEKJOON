# 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
temp = 0

for i in arr:
    temp += i
    sum_arr.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(sum_arr[b] - sum_arr[a-1])

    
