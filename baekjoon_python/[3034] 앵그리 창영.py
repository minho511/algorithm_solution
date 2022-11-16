# 수학 기하학 피타고라스 정리
# https://www.acmicpc.net/problem/3034
import sys; input=sys.stdin.readline
n, w, h = map(int, input().split())
std = (w**2+h**2)**0.5
for _ in range(n):
    k = int(input())
    if k <=std:
        print("DA")
    else:
        print("NE")