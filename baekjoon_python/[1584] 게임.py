# 2021 07 15 그래프 이론 그래프 탐색 너비우선탐색 누적합 다익스트라 0-1너비우선탐색
# https://www.acmicpc.net/problem/1584
import sys; input = sys.stdin.readline
import heapq
INF = int(1e9)
cost = [[INF]*501 for _ in range(501)] # 각좌표
graph = [[0]*501 for _ in range(501)]
n = int(input())  # 위험한 구역의 수
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 < x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(x2, x1+1):
        for j in range(y1, y2+1):
            graph[i][j] = 1
m = int(input())  # 죽음의 구역의 수
for i in range(m):
    x3, y3, x4, y4 = map(int, input().split())
    if x3 < x4:
        x3, x4 = x4, x3
    if y3 > y4:
        y3, y4 = y4, y3
    for i in range(x4, x3+1):
        for j in range(y3, y4+1):
            graph[i][j] = INF
cost[0][0] = 0  # (0,0)이 위험구역 또는 죽음의 구역이어도 영양을 미치지 않는다는 조건이 있다.
graph[0][0] = 0
dx = [-1,1,0,0]  # 상 하 좌 우 이동
dy = [0,0,-1,1]


def dikstra(start_x,start_y):
    q = []
    heapq.heappush(q, (graph[start_x][start_y], start_x, start_y))
    while q:
        cos, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>500 or ny>500:  # 게임판 밖 무시
                continue
            if graph[nx][ny] == INF:  # 죽음의 구역인경우 무시
                continue
            health = cos + graph[nx][ny]  # 현재좌표까지의 비용 + 다음좌표의 비용
            if health < cost[nx][ny]:  # 기존 nx,ny 좌표까지의 비용보다 작은 비용의 경로를 찾는다면 갱신한다.
                cost[nx][ny] = health
                heapq.heappush(q, (health, nx, ny))


dikstra(0,0)  # 0,0에서 출발
if cost[500][500] == INF:
    print(-1)  # 500, 500 까지 도달하지 못했다면 비용이 초기값인 INF일 것이다.
else:
    print(cost[500][500])
