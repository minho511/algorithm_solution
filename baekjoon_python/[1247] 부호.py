# 수학 사칙연산 임의 정밀도 / 큰 수 연산
# https://www.acmicpc.net/problem/1247
import sys; input=sys.stdin.readline

for _ in range(3):
    n =int(input())
    a = 0
    for _ in range(n):
        a += int(input())
    if a == 0:
        print(0)
    else:
        print('+' if a/abs(a)>0 else '-')