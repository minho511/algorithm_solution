# 수학 구현 문자열 그리디 알고리즘 임의 정밀도 / 큰 수 연산
# https://www.acmicpc.net/problem/1036
import sys; input=sys.stdin.readline
from collections import defaultdict
n = int(input())
graph = []
M = 0
ss = []
for _ in range(n):
    s = input().rstrip()
    if M<len(s):
        M = len(s)
    ss.append(s)

for i in range(n):
    s = ss[i]
    if len(s)<M:
        s = '~'*(M-len(s)) + s
    graph.append(list(s))
k = int(input())
vis = defaultdict(int)

for i in range(n):
    for j in range(M):
        oo = ord(graph[i][j])
        
        if oo == 126:
            continue
        if oo<65:
            vis[oo]+=int(36**(M-1-j)*(83-oo))
        else:
            vis[oo]+=int(36**(M-1-j)*(90-oo))

sorted_dict = sorted(vis.items(), key = lambda item: [item[1]], reverse = True)
candi = []
m = min(len(sorted_dict), k)

for i in range(m):
    if sorted_dict[i][0] == 90:
        m+=1
        if m > len(sorted_dict):
            break
        continue
    candi.append(sorted_dict[i][0])

ans = ""
cc = 0
for i in range(M):
    sum = cc
    for j in range(n):
        oo = ord(graph[j][M-1-i])
        if oo == 126:
            continue
        if oo in candi:
            oo = 90
        if oo <65:
            sum += oo-48
        else:
            sum += oo-55
    cc, nn = divmod(sum,36)
    if nn <= 9:
        ans += str(nn)
    else:
        ans += chr(nn+55)
if cc>0 :
    while cc>0:
        kk = cc%36
        if kk<=9:
            ans += str(kk)
        else:
            ans += chr(kk+55)
        cc=cc//36

print('0' if ans[::-1].lstrip('0') == "" else ans[::-1].lstrip('0'))