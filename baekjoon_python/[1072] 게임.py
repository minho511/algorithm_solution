# 2021 07 11 이분탐색 수학
# https://www.acmicpc.net/problem/1072
import sys
input = sys.stdin.readline
x, y = map(int, input().split())
z = int(100*y/x)
if z >= 99:
    print(-1)
else:
    end = int(1e9)
    start = 0
    while start <= end:
        mid = (start+end)//2
        k = int(100*(y+mid)/(x+mid))
        if k > z:
            end = mid-1
        else:
            start = mid+1
    print(end+1)