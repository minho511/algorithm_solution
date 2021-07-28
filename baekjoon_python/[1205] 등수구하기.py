# 2021 07 08 구현 정렬
import sys
input = sys.stdin.readline
n, new_score, p = map(int, input().split())
rank = list(map(int, input().split()))
while len(rank) > 0:
    if rank[-1] < new_score:
        rank.pop(-1)
        continue
    break
rank.append(new_score)
if len(rank) > p:
    print(-1)
else:
    print(rank.index(new_score)+1)
