# 숨바꼭질 6
n, s = map(int, input().split())
a = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

dis = []

for i in a:
    dis.append(abs(s - i))

ans = dis[0]

for i in range(1, n):
    ans = gcd(dis[i], ans)

print(ans)