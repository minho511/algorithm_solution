# 2021 07 10 브루트포스 정렬
import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    a, b = map(int, input().split())
    array.append((a,b))
array.sort()
tmp = 0
res = 0
for i in range(n):
    bene = array[i][0]-array[i][1]
    for j in range(i+1,n):
        k = array[i][0]-array[j][1]
        if k > 0:
            bene += k
    if bene > tmp:
        res = array[i][0]
        tmp = bene
print(res)