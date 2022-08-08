# 조합 0의 개수
n, m = map(int, input().split())

def fivecnt(n):
    ans = 0
    while n != 0:
        n //= 5
        ans += n
    return ans

def twocnt(n):
    ans = 0
    while n != 0:
        n //= 2
        ans += n
    return ans

print(min(twocnt(n) - twocnt(n - m) - twocnt(m), fivecnt(n) - fivecnt(n - m) - fivecnt(m)))