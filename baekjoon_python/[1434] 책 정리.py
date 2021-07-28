# 2021 07 06 그리디 수학 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(m):
    book = B[i]
    for j in range(n):
        if A[j] >= B[i]:
            A[j] -= B[i]
            break
print(sum(A))
