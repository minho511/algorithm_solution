# 2021 07 12 브루트포스
# https://www.acmicpc.net/problem/2231
n = int(input())
for i in range((len(str(n))-1)*9, n):
    d = i + sum(map(int, str(i)))
    if d == n:
        print(i)
        exit(0)
print(0)