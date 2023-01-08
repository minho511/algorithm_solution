# 수학
# https://www.acmicpc.net/problem/3123
import sys; input = sys.stdin.readline

X, Y = map(int, input().split())
n = int(input())

graph = [[0]*(Y+2) for _ in range(X+2)]

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    graph[x][y]+=1
    graph[x+1][y]+=1
    graph[x][y+1]+=1
    graph[x+1][y+1]+=1
ans = 0
for x in range(1,X+1):
    for y in range(1,Y+1):
        if graph[x][y] == 1:
            ans+=0.785398
        elif graph[x][y] == 2:
            candi = [(x-1,y-1), (x, y-1), (x-1, y), (x, y)]
            st = []
            for u in candi:
                if u in points:
                    st.append(1)
                else:
                    st.append(0)
            if st == [1, 0, 0, 1] or st == [0, 1, 1, 0]:
                ans += 1
            else:
                ans+= 0.956611
        elif graph[x][y]>2:
            ans +=1
print(ans)