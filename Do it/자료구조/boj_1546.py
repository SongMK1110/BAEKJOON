# 평균 구하기
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)

print(sum(scores) / m * 100 / n)