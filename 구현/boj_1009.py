# 분산처리
t = int(input())
a = []
b = []

for _ in range(t):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)

for i in range(t):
    temp = a[i] % 10

    if temp == 0:
        print(10)
    elif temp in [1, 5, 6]:
        print(temp)
    elif temp in [4, 9]:
        if b[i] % 2 == 0:
            print(temp ** 2 % 10)
        else:
            print(temp)
    else:
        if b[i] % 4 == 0:
            print(temp ** 4 % 10)
        else:
            print(temp ** (b[i] % 4) % 10)
