# 자료 구조 해시를 사용한 집합과 맵 트리를 사용한 집합과 맵
# https://www.acmicpc.net/problem/1269
import sys; input=sys.stdin.readline
from collections import Counter
input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = Counter(A+B)
cnt = 0

for _,c in C.items():
    if c == 1:
        cnt += 1
print(cnt)