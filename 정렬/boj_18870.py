# 좌표 압축
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num_sort = sorted(list(set(num)))
dic = {num_sort[i] : i for i in range(len(num_sort))}

for i in num:
    print(dic[i], end=' ')