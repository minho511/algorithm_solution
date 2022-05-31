# 2022 5 31 구현 문자열
# https://www.acmicpc.net/problem/9093

import sys; input = sys.stdin.readline
for _ in range(int(input())):
    print(" ".join(input()[::-1].split()[::-1]))
