# 수학 구현 시뮬레이션 사칙연산
# https://www.acmicpc.net/problem/10103
import sys; input=sys.stdin.readline

n = int(input())
A, B = 100, 100

for i in range(n):
    a, b = map(int, input().split())
    if a< b:
        A-=b
    elif a>b:
        B-=a
print(A)
print(B)