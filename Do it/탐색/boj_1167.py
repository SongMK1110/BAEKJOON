# 트리의 지름 구하기
from collections import deque

n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index + 1]
        a[s].append((e, v))
        index += 2

distance = [0] * (n+1)
visited = [False] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue: 
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]

BFS(1)
Max = 1
for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (n+1)
visited = [False] * (n+1)
BFS(Max)
distance.sort()
print(distance[n])