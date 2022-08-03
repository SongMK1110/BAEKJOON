# 스택 수열
n = int(input())
stack = []
cnt = 1
temp = True
op = []

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)

    