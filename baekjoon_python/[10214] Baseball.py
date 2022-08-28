# 구현
# https://www.acmicpc.net/problem/10214
import sys; input=sys.stdin.readline
T = int(input())
for _ in range(T):
    y, k = 0, 0
    for i in range(9):
        a, b= map(int, input().split())
        y += a
        k += b
    if y>k:
        print("Yonsei")
    elif y<k:
        print("Korea")
    else:
        print("Draw")