# 구현 정렬 애드 혹
# https://www.acmicpc.net/problem/24062
import sys; input=sys.stdin.readline

n = int(input())

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
    # print(tem)
    min = 0
    for i in range(s, e+1):
        A[i] = tem[i-s]
        # if A[i] != B[i] and check[i]:
        #     print(0); exit()
        if A[i] == B[i]:
            check[i] = True
        if i >0 and check[i-1]:
            if A[i] < B[i]:
                print(0);exit()
        if A == B:
            print(1); exit()
            
A = list(map(int, input().split()))
B = list(map(int, input().split()))
check = [False]*(n)
if A==B:
    print(1); exit()
    
merge_sort(0,n-1)
print(0)