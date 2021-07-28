# 2021 07 24 자료 구조 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/17219
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
site_pw = {}
for _ in range(n):
    site, pw = map(str, input().split())
    site_pw[site] = pw
for _ in range(m):
    site = input()[:-1]
    print(site_pw[site])