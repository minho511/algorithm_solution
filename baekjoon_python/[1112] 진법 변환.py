# 수학 구현 정수론
# https://www.acmicpc.net/problem/1112
import sys; input = sys.stdin.readline

x, b = map(int, input().split())
ans = ""
t = False

# x가 0이면 어떤 수의 진법으로 나타내더라도 0
if x==0:  
    print(0)
    exit()

# 양의 진법
if b>0: 
    p = abs(x)
    while p:
        p, q = divmod(p, b) # 몫, 나머지
        ans += str(q)
    print('-'+ans[::-1] if x<0 else ans[::-1])
# 음의 진법
else:
    p =x
    while p:
        p, q = divmod(p, b) # 몫, 나머지
        if q<0:
            p+=1
            q-=b
        ans += str(q)
    print(ans[::-1])