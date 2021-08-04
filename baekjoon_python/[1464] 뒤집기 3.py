# 2021 08 03 문자열 그리디
# https://www.acmicpc.net/problem/1464
import sys; input = sys.stdin.readline().rstrip
s = input()
a = []
for i in s:
    a.append(ord(i))
array = []
_min = min(a)
for i in range(len(a)-1, 0,-1):
    if a[i] == _min:
        array.append(i)
        array.append(i - 1)
        if a[:i-1]:
            _min = min(a[:i])
for i in array[::-1]:
    a = a[i::-1]+a[i+1:]
for i in a:
    print(chr(i), end='')
