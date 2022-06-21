# 수학 브루트포스 알고리즘 조합론 백트래킹
# https://www.acmicpc.net/problem/1759
import sys; input=sys.stdin.readline
from itertools import combinations, permutations
L, C = map(int, input().split())
char_list = list(input().rstrip().split(' '))

m = ['a','e','i','o','u']
cnt_m = 0
candi_m = []
cnt_j = 0
candi_j = []

for c in char_list:
    if c in m:
        candi_m.append(c)
        cnt_m += 1
    else:
        candi_j.append(c)
        cnt_j += 1
candi_pass = []
for i in range(1, cnt_m+1):
    for j in list(combinations(candi_m, i)):
        for q in range(2, cnt_j+1):
            if i + q == L:
                for k in list(combinations(candi_j, q)):
                    candi_pass.append(sorted(list(j+k)))
for p in sorted(set(list(map("".join, list(candi_pass))))):
    print("".join(p))
