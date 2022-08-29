# 숫자 카드2
n = int(input())
a = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in finds:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')

