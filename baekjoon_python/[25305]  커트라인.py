# 구현 정렬
# https://www.acmicpc.net/problem/25305
import sys; input=sys.stdin.readline
n, k = map(int, input().split())
scores = sorted(map(int, input().split()))
print(scores[-k])
