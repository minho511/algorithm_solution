# 문자열
# https://www.acmicpc.net/problem/10102
import sys; input=sys.stdin.readline
n = int(input())
s = input()
a_score = 0
b_score = 0
for i in s:
    if i == 'A':
        a_score+=1
    elif i == 'B':
        b_score+=1
if a_score == b_score:
    print('Tie')
elif a_score < b_score:
    print('B')
else:
    print('A')
