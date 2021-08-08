# 2021 08 08 구현 그래프 이론 그래프 탐색 너비 우선 탐색 시뮬레이션
# https://www.acmicpc.net/problem/16236
import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
graph = []
posX = 0
posY = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 시작위치를 찾는다.
        if graph[i][j] == 9:
            posX, posY = i, j

# 이동방향
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 너비우선탐색
def bfs(posx,posy):
    SIZE = 2  # 초기 상어의 사이즈 2
    eat = 2
    result = 0  # 마지막 물고기를 먹은 순간까지의 시간을 기록
    time = [[0]*n for _ in range(n)]  # 해당칸으로까지 이동하는데 걸리는 시간, 방문여부를 기록
    time[posx][posy] = 1 # 시작칸 방문처리를 위해 시작을 1로 설정 (나중에 1을 빼준값으로 시간을 결정)
    graph[posx][posy] = 0
    q = deque([(posx,posy)])
    while q:
        target_fish = []
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                # nx, ny 좌표가 범위를 벗어나면 무시
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                # nx, ny 좌표가 방문한 적 없는 칸일 때
                if time[nx][ny] == 0:
                    # 더 큰 물고기를 만나면 무시
                    if graph[nx][ny] > SIZE:
                        continue
                    # 같은 크기의 물고기를 만나면 지나갈수는 있지만 먹지 못함
                    elif graph[nx][ny] == SIZE:
                        q.append((nx, ny))
                        time[nx][ny] = time[x][y] + 1
                    # 물고기가 없다면 지나갈수 있다.
                    elif graph[nx][ny] == 0:
                        q.append((nx, ny))
                        time[nx][ny] = time[x][y] + 1
                    # 더 작은 크기의 물고기를 만나면 먹을 수 있다.
                    elif 0<graph[nx][ny] < SIZE:
                        # 같은 거리의 먹잇감 중에서 가장위, 가장 왼쪽의 물고기를 고르기위해 일단 따로 모은다
                        # 가장 먼저 찾은 물고기의 위치를 기록하고 보다 먼 거리의 먹잇감을 찾으면 무시한다
                        if not target_fish:
                            check_time = time[x][y]
                            target_fish.append((nx, ny))
                            continue
                        if target_fish and time[x][y] == check_time:
                            target_fish.append((nx, ny))
                        # 이 좌표를 지나서 가야하는 곳에 있는 물고기라면 분명 더 먼거리에 있을것이므로 지나갈 수 없다고 취급
        # 먹을 수 있는 물고기가 있다.
        if target_fish:
            eat -= 1
            # 자신보다 작은 크기의 물고기를 SIZE만큼 먹으면 SIZE+=1
            if eat == 0:
                SIZE+=1
                eat = SIZE  # eat 초기화
            result += check_time  # 1초로 시작하였으므로 -1한 값을 진행 시간에 더함
            # 가장 왼쪽 위 좌표를 찾아서 q에 추가
            target_fish.sort(key=lambda data: [data[0],data[1]])
            # 해당 좌표부터 다시 탐색을 시작해야하므로 q, time초기화
            q = deque()
            time = [[0]*n for _ in range(n)]
            time[target_fish[0][0]][target_fish[0][1]] = 1
            graph[target_fish[0][0]][target_fish[0][1]] = 0
            q.append(target_fish[0])
        # 더이상 먹을 수 있는 물고기가 없을때 종료
        else:
            return result

print(bfs(posX, posY))