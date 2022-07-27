n = int(input())
room = 1
cnt = 1

while n > room:
    room = room + (cnt * 6)
    cnt += 1

print(cnt)