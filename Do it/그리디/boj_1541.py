# 잃어버린 괄호
ans = 0
a = list(map(str, input().split("-")))

def mysum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(a)):
    temp = mysum(a[i])
    if i == 0:
        ans += temp
    else:
        ans -= temp

print(ans)