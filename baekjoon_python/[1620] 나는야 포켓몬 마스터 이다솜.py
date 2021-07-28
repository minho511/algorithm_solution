# 2021 07 22
# https://www.acmicpc.net/problem/1620
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
pokemon = {}
pokemon_rev = {}
for i in range(1, n+1):
    l = input()[:-1]
    pokemon[i] = l
    pokemon_rev[l] = i
for _ in range(m):
    s = input()[:-1]
    if s.isdigit():
        print(pokemon[int(s)])
    else:
        print(pokemon_rev[s])