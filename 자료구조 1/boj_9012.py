# 괄호
t = int(input())

for i in range(t):
    s = input()
    stack = []
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")