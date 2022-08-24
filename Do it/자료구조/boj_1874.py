# 스택 수열
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
ans = ""

for i in range(n):
    su = a[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            ans += "+\n"
        stack.pop()
        ans += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            ans += "-\n"

if result:
    print(ans)