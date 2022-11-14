# 그래프 이론 그래프 탐색 트리
# https://www.acmicpc.net/problem/25511
import sys; input=sys.stdin.readline
from collections import defaultdict, deque

n, k = map(int, input().split())
graph = defaultdict(list)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
li = list(map(int, input().split()))
q = deque([0])
depth = 0
check = False
if k == li[0]:
    print(0)
else:
    while q:
        depth+=1
        for _ in range(len(q)):
            c = q.popleft()
            for x in graph[c]:
                if li[x] == k:
                    check = True
                    break
                q.append(x)
            if check:
                break
        if check:
            break
    print(depth)