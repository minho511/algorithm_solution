# 2021 07 12 이분탐색
# https://www.acmicpc.net/problem/status/2512
import sys
input = sys.stdin.readline
n = int(input())
array = sorted(list(map(int, input().split())))
total = int(input())
if sum(array) <= total:  # 모둔 요청이 배정될 수 있는 경우에는 배정
    print(array[n-1])
else:
    result = 0
    start = 1
    end = total
    while start <= end:
        mid = (start+end)//2  # 정수 상한액
        bud = 0
        for i in array:
            bud += min(i, mid)
        if bud <= total:
            result = mid
            start = mid+1
        elif bud > total:
            end = mid-1
    print(result)
