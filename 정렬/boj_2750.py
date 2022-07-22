#수 정렬하기
n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)

# 버블 정렬
# n = int(input())

# num = []

# for _ in range(n):
#     num.append(int(input()))

# for i in range(len(num)):
#     for j in range(len(num)):
#         if num[i] < num[j]:
#             num[i], num[j] = num[j], num[i]

# for k in num:
#     print(k)