# 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
a = [[] for _ in range(n+1)]
ans = []
visited = [-1] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                queue.append(i)

for i in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

BFS(x)

for i in range(n+1):
    if visited[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)