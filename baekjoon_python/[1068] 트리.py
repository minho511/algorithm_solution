# 2021 08 02 그래프 이론 그래프 탐색 트리 깊이 우선 탐색
# https://www.acmicpc.net/problem/1068
import sys; input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
k = int(input())
graph = [[] for _ in range(n)]
top = 0

for i in range(n):
    if data[i] == -1:
        continue
    # 지울 노드와 관련된 정보는 모두 반영하지 않는다.
    if data[i] == k or i == k:
        continue
    graph[data[i]].append(i)
# 그래프에 각 인덱스값을 부모노드로 갖는 자식 노드를 담아준다.
visited = [False]*n
res = []
def dfs(v):
    visited[v] = True
    if not graph[v]:
        res.append(v)  # 자식 노드 정보가 없는 리프노드를 res에 담는다.
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(n):
    # 최상위 노드가 여러개인 경우를 고려한다.
    if data[i] == -1:
        if i == k:  # 지울노드에 대하여는 dfs를 수행하지 않는다.
            continue
        dfs(i)
print(len(res))