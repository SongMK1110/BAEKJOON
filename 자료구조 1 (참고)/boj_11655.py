# ROT13
import sys
s = sys.stdin.readline().rstrip()
ans = ''

for i in s:
    if i.isupper():
        num = ord(i) + 13
        if num > 90:
            num -= 26
        ans += chr(num)
    
    elif i.islower():
        num = ord(i) + 13
        if num > 122:
            num -= 26
        ans += chr(num)
    
    else:
        ans += i

print(ans)