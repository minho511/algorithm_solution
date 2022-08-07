# 수학 구현 사칙연산
# https://www.acmicpc.net/problem/25304
import sys; input=sys.stdin.readline

x = int(input())
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    x-=a*b
print("Yes" if x == 0 else "No")