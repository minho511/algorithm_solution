# 2021 08 02 그래프 이론 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/9019
from collections import deque
import sys; input = sys.stdin.readline

def D(num):
    return (2*num)%10000
def S(num):
    k = num-1
    if k == -1:
        return 9999
    else:
        return k

def L(num):
    l = len(str(num))
    if l == 4:
        return (num*10)%10000+num//1000
    else:
        return num*10


def R(num):
    l = len(str(num))
    return num%10 * 1000 + num//10

# 0 1 2 3
# D S L R

def DSLR(k, target):
    label = ["D", "S", "L", "R"]
    visited[k] = True
    q = deque([(k, "")])
    while q:
        now, s = q.popleft()
        if now == target:
            return s
        array = [D(now), S(now), L(now), R(now)]
        for i in range(4):
            m = array[i]
            if not visited[m]:
                visited[m] = True
                q.append((m, s+label[i]))


for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    visited = [False]*10000
    print(DSLR(a,b))