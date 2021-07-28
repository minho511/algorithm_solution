# 2021 07 16 자료 구조 문자열 스택
# https://www.acmicpc.net/problem/4949
import sys; input = sys.stdin.readline
while True:
    s = input()[:-1]
    if s == '.':
        break
    array = []
    check = False
    for i in s:
        if i == '(' or i == '[':
            array.append(i)
        if i == ')' or i == ']':
            if len(array) == 0:
                check = True
                break
            k = array.pop()
            if i == ')' and k == '[':
                check = True
                break
            if i == ']' and k == '(':
                check = True
                break
    if check or array:
        print("no")
    else:
        print("yes")