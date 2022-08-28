# 수학 정수론
# https://www.acmicpc.net/problem/9506
import sys; input=sys.stdin.readline
while True:
    n = int(input())
    if n == -1: break
    yac = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            yac.append(n//i)
            yac.append(i)
    yac.sort()
    if sum(yac[:-1]) == n:
        print(f"{n} =", " + ".join(map(str, yac[:-1])))
    else:
        print(f"{n} is NOT perfect.")