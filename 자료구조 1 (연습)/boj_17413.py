# 단어 뒤집기 2
import sys
s = list(sys.stdin.readline().rstrip())

flag = False
result = ''
stack = ''

for i in s:
    if flag == False:
        if i == '<':
            flag = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
            stack = ''
        else:
            stack = i + stack
    
    elif flag == True:
        stack += i
        if i == '>':
            flag = False
            result += stack
            stack = ''

print(result + stack)