# 수학 브루트포스 알고리즘 사칙연산
# https://www.acmicpc.net/problem/25494
import sys; input=sys.stdin.readline

T=int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    cnt = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                if i%j == j%k == k%i:
                    cnt+=1
    print(cnt)