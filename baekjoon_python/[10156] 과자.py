# 수학 사칙연산
# https://www.acmicpc.net/problem/10156
import sys; input=sys.stdin.readline
k, n, m = map(int, input().split())

print(max(k*n-m, 0))
