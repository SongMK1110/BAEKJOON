# 베르트랑 공준
num = []

for i in range(2, 2*123456+1):
    cnt = 0
    for j in range(2, int(i**0.5) +1):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        num.append(i)

while True:
    n = int(input())
    result = 0

    if n == 0:
        break
    for i in num:
        if n < i <= 2*n:
            result += 1

    print(result)
                