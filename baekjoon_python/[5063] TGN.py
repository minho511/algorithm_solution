# 수학 사칙연산
# https://www.acmicpc.net/problem/5063
import sys; input=sys.stdin.readline
n = int(input())
for _ in range(n):
    r, e, c = map(int, input().split())
    if e-c > r:
        print("advertise")
    elif e-c == r:
        print("does not matter")
    else:
        print("do not advertise")