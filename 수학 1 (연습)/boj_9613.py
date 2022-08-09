# GCD 합
t = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for i in range(t):
    n = list(map(int, input().split()))
    ans = 0
    for j in range(1, len(n)):
        for k in range(j+1, len(n)):
            ans += gcd(n[j], n[k])
    
    print(ans)
