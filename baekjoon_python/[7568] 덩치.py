# 2021 07 16 구현 브루트포스
# https://www.acmicpc.net/problem/7568
import sys; input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    array.append(tuple(map(int, input().split())))
cnt_arr = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            cnt+=1
    cnt_arr.append(cnt)
print(*cnt_arr)
