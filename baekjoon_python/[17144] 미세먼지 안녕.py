# type of problem
# link
import sys; input=sys.stdin.readline

R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

airc = [0,0]
for i in range(R):
    if graph[i][0] == -1:
        airc[0] = i
        airc[1] = i+1
        break

def diff(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    res = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or ny <0 or nx>=R or ny>=C:
            continue
        if graph[nx][ny] == -1:
            continue
        cnt += 1
        res.append((nx, ny, int(graph[x][y]*0.2)))
    res.append((x, y, -cnt*int(graph[x][y]*0.2)))
    return res

def rotate_up():
    ax = airc[0]
    for x in range(ax-1, 0, -1):
        graph[x][0] = graph[x-1][0]
    for y in range(0, C-1):
        graph[0][y] = graph[0][y+1]
    for x in range(0, ax):
        graph[x][C-1] = graph[x+1][C-1]
    for y in range(C-1, 1, -1):
        graph[ax][y] = graph[ax][y-1]
    graph[ax][1] = 0

def rotate_down():
    ax = airc[1]
    for x in range(ax+1, R-1):#  ax+1, 0/ R-2,0
        graph[x][0] = graph[x+1][0]
    for y in range(0, C-1):# R-1, 0 / R-1,C-2
        graph[R-1][y] = graph[R-1][y+1]
    for x in range(R-1, ax, -1): # ax+1, C-1 /  R-1 C-1
        graph[x][C-1] = graph[x-1][C-1] 
    for y in range(C-1, 1, -1): # 
        graph[ax][y] = graph[ax][y-1]
    graph[ax][1] = 0
        

for t in range(T):
    tem = []
    for x in range(R):
        for y in range(C):
            if graph[x][y] > 0:
                tem+=diff(x, y)

    for p in tem:
        x, y, v = p
        graph[x][y]+=v
    
    rotate_up()
    rotate_down()

ans = 0
for i in range(R):
    ans += sum(graph[i])
for i in range(R):
    print(*graph[i])
print(ans+2)


        

