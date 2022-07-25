
arr = []

for i in range(1, 10):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr))+1)