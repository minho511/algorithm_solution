# 자료 구조 문자열 해시를 사용한 집합과 맵 트리를 사용한 집합과 맵
# https://www.acmicpc.net/problem/11478
import sys; input=sys.stdin.readline
s = input()
cnt = 0
length = len(s)
for l in range(1,length):
    std = 0
    dd = set()
    for i in range(length-l):
        dd.add(s[std:std+l])
        std+=1
    cnt += len(dd)
    # for t in dd:
    #     print(t)
print(cnt)