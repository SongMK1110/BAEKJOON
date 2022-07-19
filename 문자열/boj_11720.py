# 숫자의 합
n = int(input())
num = str(input())
sum = 0

for i in range(n):
    sum += int(num[i])

print(sum)