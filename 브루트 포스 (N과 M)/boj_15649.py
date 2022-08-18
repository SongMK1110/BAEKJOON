# N과 M (1)
n, m = list(map(int, input().split()))
arr = []

def sol():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            sol()
            arr.pop()

sol()