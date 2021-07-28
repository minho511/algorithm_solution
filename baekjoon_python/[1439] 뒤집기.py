# 2021 07 07 그리디
s = input()
cnt = 0
std = 'a'
for i in s:
    if i != std:
        cnt += 1
    std = i
print(cnt//2)