# 후위 표기식2
n = int(input())
word = input()
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

stack = []

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(arr[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print(f"{stack[0]:.2f}")