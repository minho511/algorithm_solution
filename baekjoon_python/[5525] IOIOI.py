# 2021 07 24 문자열
# https://www.acmicpc.net/problem/5525
import sys; input = sys.stdin.readline
n = int(input())
input()
s = input()
target = 2*n+1
cnt = 0
state = 0  # 상태 0 1 2 3 4 ,,, 2n+1
for i in s:
    if i == 'I':
        if state % 2 == 0:
            state+=1
        else:
            state = 1
    else:
        if state % 2 == 0:
            state = 0
        else:
            state +=1
    if state == target:
        cnt += 1
        state -= 2
print(cnt)
