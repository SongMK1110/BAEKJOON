# 절댓값 힙
from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
myqueue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if myqueue.empty():
            print('0\n')
        else:
            temp = myqueue.get()
            print(str((temp[1]))+'\n')
    else:
        myqueue.put((abs(request), request))