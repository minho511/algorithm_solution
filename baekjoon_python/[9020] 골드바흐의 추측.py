# 2021 07 04 수학 정수론 소수판정 에라토스테네스의 체
import sys
input = sys.stdin.readline
graph = [1] * 10001
graph[0] = 0
graph[1] = 0
for i in range(2, 101):
    if graph[i] == 1:
        for j in range(i*i, 10001, i):
            graph[j] = 0

n = int(input())
for _ in range(n):
    x = int(input())
    std = x//2
    j = 0
    while True:
        if graph[std+j] == 1 and graph[std-j] == 1:
            print(std-j, std+j)
            break
        j+=1