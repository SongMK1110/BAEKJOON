# 과제 안 내신 분...?
a = []
for i in range(1,31):
    a.append(i)
for _ in range(1, 29):
    b = int(input())
    a.remove(b)
    
print(min(a))
print(max(a))
