# 2021 07 25 수학 자료 구조 문자열 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/9375
import sys; input = sys.stdin.readline
from collections import Counter
T = int(input())

for _ in range(T):
    n = int(input())
    clothes = []
    ans = 1
    for _ in range(n):
        tm, t = map(str, input().split())
        clothes.append(t)
    c = Counter(clothes)
    for i in c.items():
        ans *= i[1]+1
    print(ans-1)
