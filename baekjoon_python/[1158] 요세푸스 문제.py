# 자료 구조 큐
# https://www.acmicpc.net/problem/1158
import sys; input=sys.stdin.readline().rstrip
from collections import deque

n, k = map(int, input().split())
deq = deque([str(i) for i in range(1,n+1)])
output = []

while deq:    
    deq.rotate(-k+1)
    output.append(deq.popleft())
print(f"<{', '.join(output)}>")
