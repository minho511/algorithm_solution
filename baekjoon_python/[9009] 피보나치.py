# 2021 07 20 수학 그리디
# https://www.acmicpc.net/problem/9009
d = [0]*44
d[0] = 1
d[1] = 1
for i in range(2,44):
    d[i] = d[i-1]+d[i-2]
t = int(input())
for _ in range(t):
    ans = []
    n = int(input())
    i = 43
    while n>0:
        if d[i] <=n:
            n-=d[i]
            ans.append(d[i])
        i-=1
    print(*ans[::-1])