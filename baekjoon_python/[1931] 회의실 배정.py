# 2021 07 16 그리디 정렬
# https://www.acmicpc.net/problem/1931
import sys; input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(tuple(map(int,input().split())))
array.sort()
array.sort(key=lambda data:data[1])
q = array[0][1]
cnt = 1
for i in range(1,n):
    if array[i][0] >= q:
        cnt+=1
        q = array[i][1]
print(cnt)