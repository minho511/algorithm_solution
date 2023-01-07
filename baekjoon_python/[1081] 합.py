# 수학
# https://www.acmicpc.net/problem/1081
import sys; input = sys.stdin.readline
l, u = map(str, input().rstrip().split())
m = [[0] * 11 for _ in range(11)]
m[0] = [0,1,3,6,10,15,21,28,36, 45]
m[1] = [0,45,100,165,240, 325, 420, 525, 640, 765, 900]

for i in range(1, len(u)):
    m[i][1] = m[i-1][-1]
    for j in range(2,11):
        m[i][j] = m[i-1][-1]*(j)+(10**i)*(j)*(j-1)//2

def count(l):
    cntl = 0
    for i in range(len(l)-1):
        c = int(l[i])
        cntl += m[len(l)-i-1][c]
        cntl += c*(int(l[i+1:])+1)
    cntl += m[0][int(l[-1])]
    return cntl

l = str(max(int(l)-1, 0))
print(count(u)-count(l))