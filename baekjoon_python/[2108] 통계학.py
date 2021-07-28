# 2021 07 14 구현 정렬
# https://www.acmicpc.net/problem/2108
import sys; input=sys.stdin.readline
n = int(input())
array = []
feq = [0]*8001
for i in range(n):
    k = int(input())
    array.append(k)
    feq[k+4000] += 1
array.sort()
mx_feq = max(feq)
res_feq = 0
cnt = 0
for i in range(8001):
    if feq[i] == mx_feq:
        cnt+=1
        if cnt == 2:
            res_feq = i-4000
            break
        res_feq = i-4000
print(round(sum(array)/n),array[n//2],res_feq,array[-1]-array[0],sep='\n')
