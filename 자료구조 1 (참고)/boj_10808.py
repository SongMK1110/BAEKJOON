# 알파벳 개수
s = input()
alpha = list(range(97,123))

for i in alpha:
    print(s.count(chr(i)), end=' ')