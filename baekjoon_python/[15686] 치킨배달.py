# 구현 브루트포스 백트래킹
# https://www.acmicpc.net/problem/15686
import sys; input=sys.stdin.readline
from itertools import combinations
N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

one = []
two = []
for x in range(N):
    for y in range(N):
        if city[x][y] == 1:
            one.append((x, y))
        elif city[x][y] == 2:
            two.append((x, y))

ans = []
for com in combinations(two, M):
    t = 0
    for x, y in one:
        dis = []
        for x1, y1 in com:
            dis.append(abs(x-x1) + abs(y-y1))
        t+=min(dis)
    ans.append(t)
print(min(ans))

