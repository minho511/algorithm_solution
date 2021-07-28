# 2021 07 27 그래프 이론 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/16928
import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
cnt = [0] *101
visited = [False] *101
snk = []
lad = []
for _ in range(n):
    a, b = map(int, input().split())
    lad.append((a,b))
for _ in range(m):
    a, b = map(int, input().split())
    snk.append((a,b))
q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    for i in range(1,7):
        nx = x + i
        if nx >100:
            continue
        if not visited[nx]:
            for ladder in lad:
                if ladder[0] == nx:
                    nx = ladder[1]
                    break
            for snake in snk:
                if snake[0] == nx:
                    nx = snake[1]
                    break
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                cnt[nx] = cnt[x]+1
print(cnt[100])