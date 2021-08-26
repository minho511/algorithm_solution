# 2021 08 25 다이나믹 프로그래밍 그래프 이론 문자열 그래프 탐색 너비 우선 탐색
# https://www.acmicpc.net/problem/9177
from collections import deque
import sys; input = sys.stdin.readline

def bfs(word1, word2, target):
    l1 = len(word1)
    l2 = len(word2)
    v = [[False] * (l2+1) for _ in range(l1+1)]
    q = deque([(0,0)])
    cnt = 0
    while q:
        for _ in range(len(q)):
            i1, i2 = q.popleft()
            if i1 < l1 and word1[i1] == target[cnt] and not v[i1+1][i2]:
                q.append((i1+1, i2))
                v[i1+1][i2] = True
            if i2 < l2 and word2[i2] == target[cnt] and not v[i1][i2+1]:
                q.append((i1, i2+1))
                v[i1][i2+1] = True
        cnt += 1
    if cnt == len(target)+1:
        return True
    return False

for i in range(int(input())):
    w1, w2, target = map(str, input().split())
    if w1 + w2 == target or w2 + w1 == target:
        print("Data set {}: yes".format(i + 1))
    elif bfs(w1, w2, target):
        print("Data set {}: yes".format(i + 1))
    else:
        print("Data set {}: no".format(i + 1))