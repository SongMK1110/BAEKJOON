# 단어 뒤집기
import sys
t = int(input())

for i in range(t):
    word = sys.stdin.readline().split()

    for j in word:
        print(j[::-1], end=' ')
    print()