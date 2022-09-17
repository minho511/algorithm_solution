# 수학 기하학 이분 탐색 피타고라스 정리
# https://www.acmicpc.net/problem/2022

import sys; input=sys.stdin.readline

x, y, c = map(float, input().split())

def bin(m):
    a = (x**2 - m**2)**0.5
    b = (y**2 - m**2)**0.5
    return (a*b)/(a+b)

start = 0
end = min(x, y)
ans = 0
while end-start > 1e-6:
    mid = (end+start)/2
    if bin(mid)>=c:
        start = mid
    else:
        end = mid
print(round(start, 3))
    