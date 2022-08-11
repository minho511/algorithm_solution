# type of problem
# link
import sys; input=sys.stdin.readline

w, h, x, y, p = map(int, input().split())
cnt = 0
for _ in range(p):
    a, b = map(int, input().split())
    p1 = (x, y+h//2)
    p2 = (x+w, y+h//2)
    
    if a<x:
        distance = (abs((a-p1[0])**2+(b-p1[1])**2))**0.5
        if distance <= h//2:
            cnt += 1
    elif a>x+w:
        distance = (abs((a-p2[0])**2+(b-p2[1])**2))**0.5
        if distance <= h//2:
            cnt +=1
    else:
        if y<=b<=y+h:
            cnt += 1
print(cnt)