# 오큰수
n = int(input())
number = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and number[stack[-1]] < number[i]:
        answer[stack.pop()] = number[i]
    stack.append(i)

print(*answer)