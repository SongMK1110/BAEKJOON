# 요세푸스 문제
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

answer = []
num = 0

for i in range(n):
    num += k - 1
    if num >= len(arr):
        num %= len(arr)
    answer.append(str(arr.pop(num)))

print("<",", ".join(answer),">", sep='')
