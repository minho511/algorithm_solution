# 수학 문자열
# https://www.acmicpc.net/problem/1334
import sys; input=sys.stdin.readline

n = int(input())+1
fn = n
# 자리수
l = len(str(n))
if l == 1:
    print(n)
else:
    while True:
        s = list(str(n))
        left = s[:l//2]
        p = s
        if l%2 == 1:
            p[-l//2+1:] = left[::-1]
            if int("".join(p)) < fn:
                for i in range(l//2+1):
                    if s[l//2-i] != '9':
                        s[l//2-i] = str(int(s[l//2-i])+1)
                        break
                    s[l//2-i] ='0'
                n = int("".join(s))
            else:
                print("".join(p))
                break    
        else:
            p[-l//2:] = left[::-1]
            if int("".join(p)) < fn:
                for i in range(l//2):
                    if s[l//2-1-i] != '9':
                        s[l//2-1-i] = str(int(s[l//2-1-i])+1)
                        break
                    s[l//2-1-i] = '0'
                n = int("".join(s))
            else:
                print("".join(p))
                break