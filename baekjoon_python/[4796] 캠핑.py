# 2021 07 07 그리디
import sys
input = sys.stdin.readline
case = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    case +=1
    print("Case {}:".format(case), V//P*L+min(V % P,L))
