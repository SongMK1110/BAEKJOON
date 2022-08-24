# 오큰수 구하기
n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
mystack = []

for i in range(n):
    while mystack and a[mystack[-1]] < a[i]:
        ans[mystack.pop()] = a[i]
    mystack.append(i)

while mystack:
    ans[mystack.pop()] = -1

result = ""

for i in range(n):
    result += str(ans[i])+" "

print(result)