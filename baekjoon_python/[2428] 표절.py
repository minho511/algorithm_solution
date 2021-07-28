# 2021 07 11 정렬 이분 탐색 슬라이딩 윈도우
# https://www.acmicpc.net/problem/2428
import sys
input = sys.stdin.readline
n = int(input())
file = list(map(int, input().split()))
file.sort()
cnt = 0
for i in range(n):
    k = file[i]
    start = i+1
    end = n-1
    point = 0
    while start<=end:
        mid = (start+end)//2
        if 0.9 * file[mid] <= k:
            start = mid+1
        else:
            end = mid-1
    cnt += end-i
print(cnt)