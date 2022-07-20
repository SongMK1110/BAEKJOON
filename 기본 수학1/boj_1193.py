# 분수찾기
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

d = end - n

if line % 2 == 0:
    top = line - d
    bottom = d + 1
else:
    top = d + 1
    bottom = line - d

print(f"{top}/{bottom}")

