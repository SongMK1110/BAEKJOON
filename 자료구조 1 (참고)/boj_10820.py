# 문자열 분석
import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    up, lo, sp, num = 0, 0, 0, 0

    if not s:
        break

    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            lo += 1
        elif i.isspace():
            sp += 1
        elif i.isdigit():
            num += 1
    
    print(lo, up, num, sp)