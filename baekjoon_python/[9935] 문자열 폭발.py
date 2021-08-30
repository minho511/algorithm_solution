# 2021 08 30 자료 구조 문자열 스택
# https://www.acmicpc.net/problem/9935
import sys; input = sys.stdin.readline
s = input().rstrip()
e = list(input().rstrip())
el = len(e)
sl = len(s)

array = []
for i in range(sl):
    array.append(s[i])
    if s[i] == e[-1] and array[-el:] == e:
        del array[-el:]
if array:
    print("".join(array))
else:
    print("FRULA")