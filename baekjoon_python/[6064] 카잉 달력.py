# 2021 07 28 수학 정수론 중국인의 나머지 정리
# https://www.acmicpc.net/problem/6064
import sys; input =sys.stdin.readline
def kaing(m, n, x, y):
    if x == y:
        return x
    if m > n:
        m,n = n, m
        x,y = y,x
    k = x
    cnt = x
    q = n-m
    check = False
    while True:
        k -= q
        if k <= 0:
            k+=n
        cnt += m
        if k == y:
            break
        if k == x:
            check = True
            break
    if check:
        return -1
    else:
        return cnt

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(kaing(m,n,x,y))