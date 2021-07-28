# 2021 07 20 자료 구조 문자열 트리를 사용한 집합과 맵
# https://www.acmicpc.net/problem/14425
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
s = {}
cnt = 0
for _ in range(n):
    s[input()] = 1
for _ in range(m):
    check = input()
    cnt+=s.get(check,0)
print(cnt)