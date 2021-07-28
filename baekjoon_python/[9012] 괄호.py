# 2021 07 14 자료구조 문자열 스택
# https://www.acmicpc.net/problem/9012
t = int(input())
for _ in range(t):
    s = input()
    n= len(s)
    if s[0] == '(' and s[-1] == ')':
        cnt = 0
        for i in range(0, n):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt < 0:
                    break
        if cnt == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")