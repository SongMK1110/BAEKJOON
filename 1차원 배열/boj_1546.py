# 평균
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
new_list = []

for i in scores:
    new_list.append(i / m * 100)

print(sum(new_list) / n)
