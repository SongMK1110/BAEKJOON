# 명령 프롬프트
n = int(input())
arr = list(input())
arr_len = len(arr)

for i in range(n-1):
    file = list(input())
    for j in range(arr_len):
        if arr[j] != file[j]:
            arr[j] = '?'

print(''.join(arr))