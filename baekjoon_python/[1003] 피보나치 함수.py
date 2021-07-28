#백준 1003
import sys
T = int(sys.stdin.readline())
dpt0 = [0]*41
dpt1 = [0]*41
dpt0[0] = 1
dpt0[1] = 0
dpt1[0] = 0
dpt1[1] = 1
for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(2, n+1):
        dpt0[i] = dpt0[i-1] + dpt0[i-2]
        dpt1[i] = dpt1[i-1] + dpt1[i-2]
    print(dpt0[n], dpt1[n])