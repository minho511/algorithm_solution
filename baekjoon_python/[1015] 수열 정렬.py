# 2021 07 28 정렬
# https://www.acmicpc.net/problem/1015
n = int(input())
array = list(map(int, input().split()))
tm = sorted(array)
for i in array:
    k = tm.index(i)
    tm[k] =-1
    print(k,end=' ')