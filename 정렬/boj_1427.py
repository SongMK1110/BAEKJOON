# 소트인사이드
n = int(input())

li = []

for i in str(n):
    li.append(int(i))

li.sort(reverse=True)

for j in li:
    print(j, end='')