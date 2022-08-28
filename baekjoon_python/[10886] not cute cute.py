# 수학 구현 사칙연산
# https://www.acmicpc.net/problem/10886
import sys; input=sys.stdin.readline
n = int(input())
sur = 0
for _ in range(n):
    sur += int(input())

check = "not " if sur <= n//2 else ""
print(f"Junhee is {check}cute!")