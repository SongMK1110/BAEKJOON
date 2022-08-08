# 최소공배수
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    A, B = a, b
    while b != 0:
        a, b = b, a % b
        
    print(A * B // a)