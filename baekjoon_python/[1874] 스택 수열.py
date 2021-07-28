# 2021 07 13 자료구조 스택
# acmicpc.net/problem/1874
import sys;input = sys.stdin.readline
n = int(input())
array = []  # 수열
stack = []  # 스택
s = ""  # 정답을 담을 문자열
for i in range(n):
    array.append(int(input()))
array = array[::-1]
check = True
i = 1
cnt = 0
while array:
    while i <= array[-1]:
        stack.append(i)
        s += "+\n"
        i += 1
    while len(stack)>0 and len(array)>0 and stack[-1] == array[-1]:
        stack.pop()
        array.pop()
        s += "-\n"
    cnt+=1
    if cnt > n:
        check = False
        break
if check:
    print(s)
else:
    print("NO")