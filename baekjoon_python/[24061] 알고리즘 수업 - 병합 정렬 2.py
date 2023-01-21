# 구현 정렬 재귀
# https://www.acmicpc.net/problem/24061
import sys; input=sys.stdin.readline

def merge_sort(s, e):
    m = (s+e)//2
    # print(s, m, e)
    if s == m == e:
        return
    merge_sort(s, m)
    merge_sort(m+1, e)
    merge(s, m, e)
    
def merge(s, m, e):
    global cnt
    i = s
    j = m+1
    tem = []
    while i <= m and j <=e:
        if A[i] < A[j]:
            tem.append(A[i])
            i+=1
        else:
            tem.append(A[j])
            j+=1
    while i <=m:
        tem.append(A[i])
        i+=1
    while j <=e:
        tem.append(A[j])
        j+=1
    for i in range(s, e+1):
        A[i] = tem[i-s]
        cnt +=1
        if cnt==k:
            print(*A)
            exit()
    

n, k = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
merge_sort(0, len(A)-1)
print(-1)