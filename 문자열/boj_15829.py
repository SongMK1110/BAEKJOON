# Hashing
L = int(input())
s = input()
result = 0

for i in range(L):
    result += (ord(s[i])-96) * (31 ** i)
print(result % 1234567891)