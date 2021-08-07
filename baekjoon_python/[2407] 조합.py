# 2021 08 07 수학 다이나믹 프로그래밍 조합론 임의 정밀도 / 큰 수 연산
# https://www.acmicpc.net/problem/2407

def op(a, b):  # a * a+1 * a+2 * ... * b
    k = 1
    for i in range(a, b+1):
        k*=i
    return k


n, m = map(int, input().split())
print(op(m+1, n)//op(1,n-m))