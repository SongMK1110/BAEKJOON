# 전자레인지
t = int(input())
button = [300, 60, 10]
answer = [0, 0, 0]

for i in range(len(button)):
    answer[i] = t // button[i]
    t = t % button[i]
    if t == 0:
        print(*answer)
        break
else:
    print(-1)




