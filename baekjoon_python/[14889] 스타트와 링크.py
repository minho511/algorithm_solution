# 브루트포스 알고리즘 백트래킹
# https://www.acmicpc.net/problem/14889
import sys; input=sys.stdin.readline
from itertools import combinations, permutations
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

min_diff = int(1e9)
for team1 in combinations(range(n), n//2):
    team2 =[]
    for i in range(n):
        if i not in team1:
            team2.append(i)
            if len(team2) == n//2:
                break
    s1, s2 = 0, 0
    for c in permutations(team1, 2):
        s1+=a[c[0]][c[1]]
    for c in permutations(team2, 2):
        s2+=a[c[0]][c[1]]
    diff = abs(s1-s2)
    if diff<min_diff:
        min_diff = diff
print(min_diff)