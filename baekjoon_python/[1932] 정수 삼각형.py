#백준 1932
#2021 06 25
import sys
input = sys.stdin.readline

n = int(input())
tri = [0]*n
d = [[0]*n for i in range(n)]
for i in range(0, n):
    tri[i] = list(map(int, input().split()))
d[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = d[i-1][j] + tri[i][j]
        elif j < i:
            d[i][j] = tri[i][j] + max(d[i-1][j-1], d[i-1][j])
        else:
            d[i][j] = d[i-1][j-1] + tri[i][j]

print(max(d[n-1]))
