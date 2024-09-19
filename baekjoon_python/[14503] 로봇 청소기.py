import sys; input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

cvt = [0, 3, 2, 1]
d = cvt[d]

room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 0

while True:    
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[x][y] == 0:
        room[x][y] = 2 # 2 -> 청소된 칸
        cnt+=1
    clean = False

    # 방향 계산 무조건 90 도 반시계로 돌고 시작
    direction = [(d+i+1)%4 for i in range(4)]
    for i in direction:    
        nx, ny = x+dx[i], y+dy[i] 
        if room[nx][ny] != 0: continue
        clean = True # 청소할 칸이 있었음
        x, y = nx, ny
        d = i
        break
    if clean: continue

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    nx, ny = x+dx[d]*-1, y+dy[d]*-1
    if room[nx][ny] == 1:  # 벽이면
        print(cnt)
        exit() # 종료
    # 아니면 후진
    x, y = nx, ny
