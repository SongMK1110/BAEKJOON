# 보물
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

for i in sorted(a):
    answer += i * max(b)
    b.pop(b.index(max(b)))

print(answer)