# 2021 08 03 자료 구조 문자열 스택 재귀
# https://www.acmicpc.net/problem/2800
from itertools import combinations
import sys; input = sys.stdin.readline().rstrip
s = input()
# 괄호쌍의 인덱스를 얻는다.
stack = []
array = []  # 괄호쌍의 인덱스를 저장
k = []  # 괄호를 공백으로 대체하여 저장
q = []  # 정답을 담을 리스트
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
        k.append(" ")
    elif s[i] == ')':
        array.append([stack.pop(),i])
        k.append(" ")
    else:
        k.append(s[i])
for i in range(len(array)):  # 괄호쌍을 선택하는 모든 경우의 수
    for j in combinations(array, i):
        tm = k[:]
        for l in j:  # 괄호쌍의 좌표 ( '('의 인덱스, ')'의 인덱스)
            tm[l[0]] = '('
            tm[l[1]] = ')'
        q.append("".join(tm).replace(" ",''))
q = sorted(list(set(q)))  # 중복되는 값을 제거  (((1+2)))에서 중복되는 경우를 발견
print('\n'.join(q))