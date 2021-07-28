# 2021 07 23 분할정복 재귀
# https://www.acmicpc.net/problem/1074
n, r, c = map(int, input().split())
res = 0
while n>0:
    t = 2**(2*n-2)
    std = 2**(n-1)
    if r<std and c<std:
        area = 0
    elif r < std <= c:
        area = 1
        c -= std
    elif r >= std > c:
        area = 2
        r-=std
    elif r >= std and c >= std:
        area = 3
        c-=std
        r-=std
    res += area * t
    n-=1
print(res)