# 셀프 넘버
def d(n):
    number = int(n)     # 33번이 들어오면
    for i in list(str(n)):   # 리스트로 쪼개서 [3,3]으로 나누고
        number += int(i)     # 33 + 3 + 3
    return number

arr = []

for i in range(1, 10001):
    arr.append(d(i))    # 셀프 넘버 아닌 수를 넣어줌

for j in range(1, 10001):
    if j in arr:
        pass
    else:
        print(j)
