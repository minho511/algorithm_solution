# 2021 08 11 수학 분할 정복을 이용한 거듭제곱
# https://www.acmicpc.net/problem/11444

def mul_matrix(m1, m2):
    res = [[(m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0])%1000000007,
            (m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1])%1000000007],
            [(m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0])%1000000007,
             (m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1])%1000000007]]
    return res

def oper(m, n):
    if n>1:
        m = oper(m, n//2)
        m = mul_matrix(m,m)
        print(m)
        if n%2==1:
            M1 = [[1, 1], [1, 0]]
            m = mul_matrix(m, M1)
    return m

n = int(input())
M1 = [[1,1],[1,0]]
print(oper(M1, n-1)[0][0]%1000000007)