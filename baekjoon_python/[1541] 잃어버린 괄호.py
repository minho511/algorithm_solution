# 2021 07 25 수학 문자열 그리디 알고리즘 파싱
# https://www.acmicpc.net/problem/1541
s = input()
if '-' not in s:
    print(eval(s))
    exit()
k = s.split('-')
for i in range(len(k)):
    sum = 0
    nums = k[i].split('+')
    for j in nums:
        sum += int(j.lstrip('0'))
    k[i] = sum
std = k[0]
for i in range(1, len(k)):
    std-=k[i]
print(std)