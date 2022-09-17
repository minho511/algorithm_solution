# 기하학 다각형의 넓이
# https://www.acmicpc.net/problem/2166
import sys; input=sys.stdin.readline
# 신발끈 공식을 사용한 풀이

n = int(input())
m1, m2 = 0,0
temx, temy = 0,0

for i in range(n):
    x,y =map(int, input().split())
    if i == 0:
        fx, fy = x, y
    m1 += temx*y
    m2 += temy*x
    temx = x
    temy = y
m1 += temx*fy
m2 += temy*fx
print(round(abs(m1-m2)/2,1))




