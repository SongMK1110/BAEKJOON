# N과 M (4)
n, m = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
visited = [False] * n
ans = []

def sol():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(n):
        if not visited[i]:
            ans.append(num[i])
            visited[i] = True
            sol()
            visited[i] = False
            ans.pop()

sol()