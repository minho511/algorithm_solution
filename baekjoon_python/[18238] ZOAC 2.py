# 2021 07 07 구현 문자열 그리디
s = input()
time = 0
now = 65
for i in s:
    next = ord(i)
    k = abs(next-now)
    time += min(k, 26-k)
    now = next
print(time)
