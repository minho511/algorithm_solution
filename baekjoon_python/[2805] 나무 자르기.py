# 2021 07 16 이분탐색
# https://www.acmicpc.net/problem/2805
import sys; input = sys.stdin.readline
from collections import Counter
n, m = map(int, input().split())
tree = Counter(map(int, input().split()))
start = 0
end = max(tree)
result = 0
while start <= end:
    h = (start + end)//2
    get = 0
    for i, cnt in tree.items():
        if i>=h:
            get += (i-h)*cnt
    # 자른 나무의 합이 목표보다 적을 때 절단기의 높이를 낮춰야 한다.
    if get < m:
        end = h-1
    # 자른 나무의 합이 충분할때 절단기의 높이를 높인다.
    else:
        start = h+1
        result = h
print(result)