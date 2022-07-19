# 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
t = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            t += dial.index(j) + 3

print(t)