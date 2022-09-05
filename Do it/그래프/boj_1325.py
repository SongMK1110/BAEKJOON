# 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
ans = [0] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i]:
                visited[i] = True
                ans[i] += 1
                queue.append(i)

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

for i in range(1, n+1):
    visited = [False] * (n+1)
    BFS(i)

maxVal = 0
for i in range(1, n+1):
    maxVal = max(maxVal, ans[i])

for i in range(1, n+1):
    if maxVal == ans[i]:
        print(i, end=' ')