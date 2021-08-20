# 2021 08 11 트리 분할 정복 재귀
# https://www.acmicpc.net/problem/2263
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
check = [0] * (n+1)
for i in range(n):
    check[inorder[i]] = i

def toPreorder(si, ei, sp, ep):
    if ei - si < 0 or ep < sp:
        return
    print(postorder[ep], end=' ')

    rootIndex = check[postorder[ep]]
    toPreorder(si, rootIndex-1, sp, sp+rootIndex-1-si)
    toPreorder(rootIndex +1, ei, sp+rootIndex-si , ep-1)

toPreorder(0, n-1, 0, n-1)