# 2021 08 30 수학 분할 정복 분할 정복을 이용한 거듭제곱 선형대수학
# https://www.acmicpc.net/problem/10830
import sys; input = sys.stdin.readline

def matrix_sqared(mat, k):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                res[i][j] += mat[i][p]*mat[p][j]
    for i in range(n):
        for j in range(n):
            res[i][j]%=1000
    d.append(res)
    if k == 1:
        return
    else:
        matrix_sqared(res, k-1)

def matrix_mul(mat1, mat2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                res[i][j] += mat1[i][p] * mat2[p][j]
    for i in range(n):
        for j in range(n):
            res[i][j] %= 1000
    return res

n, b = map(int, input().split())
matrix = []
bin_b = bin(b)
m = len(str(bin_b))-3
for _ in range(n):
    matrix.append(list(map(int, input().split())))
if b == 1:
    for i in range(n):
        for j in range(n):
            print(matrix[i][j]%1000, end=' ')
        print()
    exit(0)
d = [matrix]
matrix_sqared(matrix, m)
# 단위행렬
result = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            result[i][j] = 1
j=0
for i in str(bin_b)[::-1]:
    if i == '1':
        result = matrix_mul(result, d[j])
    elif i == 'b':
        break
    j+=1
for i in range(n):
    print(*result[i])
