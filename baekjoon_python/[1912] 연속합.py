# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1912
import sys; input=sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
accum = [a[0]]
for i in range(len(a) - 1):
    accum.append(max(accum[i] + a[i + 1], a[i + 1]))
print(max(accum))
#n = int(input())
#a = list(map(int, input().split()))
#accum = [0,a[0]]
#for i in range(1,n):
#    accum.append(accum[i]+a[i])
#M = -1000*n
#for i in range(1, n+1):
#    for j in range(i,n+1):
#        s = accum[j]-accum[j-i]
#        if s > M:
#            M = s
#print(M)