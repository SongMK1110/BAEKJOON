# 크로아티아 알파벳
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in cro_list:
    s = s.replace(i, 'a')

print(len(s))