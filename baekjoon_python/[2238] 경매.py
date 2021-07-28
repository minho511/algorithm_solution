import sys
input = sys.stdin.readline
u, n = map(int,input().split())
array = [[0] for _ in range(u+1)]
for _ in range(n):
    s, p = map(str, input().split())
    array[int(p)].append(s)
    array[int(p)][0] += 1       # array[가격 p]에 [(같은가격 제시한 사람 수), 사람1, 사람2 ,,]
m = int(100001)                 # n의 범위가 [1,100000)이므로 같은 가격을 제시한 사람이 100001명을 넘을 수 없다.
for i in range(u):
    if array[i][0] != 0:        # 가장 적은 수이 사람이 제시한 가격을 찾는다.
        if array[i][0] < m:
            m = array[i][0]
for i in range(u):              # 가장먼저 가격을 제시한 사람이 array[i][1]에 저장되어있다.
    if array[i][0] == m:
        print(array[i][1], i)
        break