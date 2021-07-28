# 그리디 알고리즘
# 2021 07 01 1800
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
node = list(map(int, input().split()))
cost = 0
min_price = node[0]
for i in range(n-1):
    if min_price > node[i]:
        min_price = node[i]
    cost += min_price * dist[i]
print(cost)