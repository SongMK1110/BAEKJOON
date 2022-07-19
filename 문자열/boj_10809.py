# 알파벳 찾기
s = input()
a = list(range(97,123))

for i in a:
    print(s.find(chr(i)), end=' ')