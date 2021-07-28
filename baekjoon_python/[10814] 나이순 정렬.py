# 2021 07 14 정렬
# https://www.acmicpc.net/problem/10814
import sys; input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    age, name = map(str, input().split())
    q.append((int(age), i, name))
q.sort(reverse=True)
while q:
    k = q.pop()
    print(k[0],k[2])