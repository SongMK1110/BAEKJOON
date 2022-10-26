# 거스름돈
n = int(input())
n = 1000-n
coin = [500, 100, 50, 10, 5, 1]
answer = 0

for i in coin:
    answer += n // i
    n = n % i
    if n == 0:
        break

print(answer)