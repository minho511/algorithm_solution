# 수학 그리디알고리즘 정렬
# https://www.acmicpc.net/problem/1026
import sys; input=sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(n):
    ans += A[i]*B[i]
print(ans)
