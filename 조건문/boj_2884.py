# 알람 시계
H, M = map(int, input().split())

if M >= 45:
    print(H,M-45)
elif M < 45 and H >= 1:
    print(H-1,M+15)
elif M < 45 and H == 0:
    print(23,M+15)