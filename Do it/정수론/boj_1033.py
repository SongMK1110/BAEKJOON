# 칵테일 만들기
n = int(input())
A = [[] for _ in range(n)]
visited = [False] * (n)
d = [0] * n
lcm = 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            d[next] = d[v] * i[2] // i[1]
            DFS(next)

for i in range(n-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

d[0] = lcm
DFS(0)
mgcd = d[0]

for i in range(1, n):
    mgcd = gcd(mgcd, d[i])

for i in range(n):
    print(int(d[i] // mgcd), end=' ')