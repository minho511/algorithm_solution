# 2021 07 13 구현 자료 구조 시뮬레이션 큐
# https://www.acmicpc.net/problem/1966
import sys; input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int,input().split()))
    q = deque()
    cnt = 0
    for i in range(n):
        q.append((priority[i], i))
    while q:
        check = True
        now = q.popleft()  # 가장 앞의 문서를 꺼내서 우선순위를 비교한다.
        for a in range(len(q)):
            if q[a][0] > now[0]:
                q.append(now)  # 만약 나머지 문서에 우선순위가 높은 문서가 있으면 후순위로 다시 넣는다.
                check = False
                break
        if check:
            cnt += 1
            if now == (priority[m], m):  # 원하는 문서가 출력됨
                print(cnt)