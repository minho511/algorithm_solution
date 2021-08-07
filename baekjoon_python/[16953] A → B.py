# 2021 08 07 그래프 이론 그리디 알고리즘 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/16953
import sys; input = sys.stdin.readline
from collections import deque

def oper1(a):
    return a//2

def oper2(a):
    return a//10

def bfs(start,target):
    k = target
    cnt = 0
    while True:
        cnt += 1
        op1 = oper1(k)
        op2 = oper2(k)
        if k == start:
            print(cnt)
            return
        # 두 연산값이 모두 start값보다 작아질때까지 start값을 만들지 못하면 만들 수 없는 target값으로 판단
        if op1 < start and op2 < start:
            print(-1)
            return
        # 우선 일의 자리가 1이라면 oper2를 수행하는 것이 연산의 최솟값을 찾는 방향
        if k%10 == 1:
            k = op2
        else:
            if k%2 == 0:
                k = op1
            else:
                # 일의자리가 1이 아닌 x가 2로도 나눠떨어지지 않으면 만들수 없는 target값으로 판단
                print(-1)
                return

a, b = map(int, input().split())
bfs(a, b)