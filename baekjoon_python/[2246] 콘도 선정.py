# 2021 07 10 구현 브루트포스 정렬
# https://www.acmicpc.net/problem/2246
import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
cnt = 0
array.sort()
for i in range(n):
    check =True
    for j in range(i):
        if array[i][0] >= array[j][0]:
            if array[i][1] >= array[j][1]:
                check = False
                break
    if check:
        cnt +=1
print(cnt)