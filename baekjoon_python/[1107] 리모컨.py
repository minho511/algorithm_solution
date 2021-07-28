# 2021 07 25 브루트포스
# https://www.acmicpc.net/problem/1107
import sys; input = sys.stdin.readline
n = int(input())  # 이동하려고 하는 채널   //   현재채널 100
m = int(input())  # 고장난 버튼 개수
broken = list(map(int, input().split()))  # 고장난 버튼 번호
res = abs(n-100)
if n == 100:
    print(0)
    exit()
if m == 10:
    print(abs(n-100))
    exit()
for i in range(1000001):
    check = True
    for j in str(i):
        if int(j) in broken:
            check = False
            break
    if check:
        res = min(res, abs(i-n)+len(str(i)))
print(res)
