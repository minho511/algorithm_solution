# 2021 07 10 구현 정렬
# https://www.acmicpc.net/problem/2693
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    array = sorted(list(map(int, input().split())))
    print(array[-3])