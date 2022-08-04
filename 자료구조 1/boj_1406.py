# 에디터
import sys
stack_1 = list(sys.stdin.readline().rstrip())
stack_2 = []
n = len(stack_1)
m = int(input())

for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == "L" and stack_1:
        stack_2.append(stack_1.pop())
    elif command[0] == "D" and stack_2:
        stack_1.append(stack_2.pop())
    elif command[0] == "B" and stack_1:
        stack_1.pop()
    elif command[0] == "P":
        stack_1.append(command[1])

print("".join(stack_1 + list(reversed(stack_2))))