# N과 M (4)
n, m = list(map(int, input().split()))
arr = []

def sol(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n+1):
        arr.append(i)
        sol(i)
        arr.pop()

sol(1)

