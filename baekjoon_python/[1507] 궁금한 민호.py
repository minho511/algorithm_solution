
# 그래프 이론 플로이드–워셜
# https://www.acmicpc.net/problem/1507
import sys; input=sys.stdin.readline

n = int(input())
graph = []
mm = []
ans = 0

for _ in range(n):
    inp = list(map(int, input().split()))
    graph.append(inp)
    mm.append(inp[:])

for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            if k == j or k== i:
                continue
            if graph[i][k] + graph[k][j] == graph[i][j]:
                mm[i][j] = 0
            elif graph[i][k] + graph[k][j] < graph[i][j]:
                print(-1)
                exit()
    ans += sum(mm[i][i+1:])
    
print(ans)