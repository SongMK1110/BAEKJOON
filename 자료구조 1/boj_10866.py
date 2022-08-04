# 덱
import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for i in range(n):
    word = sys.stdin.readline().split()

    if word[0] == "push_front":
        dq.appendleft(word[1])
    
    elif word[0] == "push_back":
        dq.append(word[1])
    
    elif word[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    
    elif word[0] == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif word[0] == "size":
        print(len(dq))
    
    elif word[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif word[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    
    elif word[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])