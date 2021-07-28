# 2021 07 13 브루트포스
# https://www.acmicpc.net/problem/1436
n = int(input())
d = [666]
i =666
while len(d)<n:
    i += 1
    if str(i).count('666') >= 1:
        d.append(i)
print(d[-1])
