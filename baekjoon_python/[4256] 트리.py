# 2021 08 20 트리 분할 정복 재귀
# https://www.acmicpc.net/problem/4256

def toPostorder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    root = inorder.index(preorder[0])
    left_in = inorder[:root]
    left_pre = preorder[1:1+len(left_in)]
    toPostorder(left_pre, left_in)

    right_in = inorder[root+1:]
    right_pre = preorder[len(left_pre)+1:]
    toPostorder(right_pre, right_in)

    print(preorder[0], end=' ')

import sys; input = sys.stdin.readline
for _ in range(int(input())):
    node = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    toPostorder(preorder, inorder)
    print()