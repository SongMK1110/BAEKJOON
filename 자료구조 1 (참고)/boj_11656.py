# 접미사 배열
s = input()
stack = []

for i in range(len(s)):
    stack.append(s[i:])

stack.sort()

for i in stack:
    print(i)
    



