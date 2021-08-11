# 2021 08 10 트리 재귀
# https://www.acmicpc.net/problem/1991
import sys; input = sys.stdin.readline
n = int(input())
tree = [[]for _ in range(n)]
for _ in range(n):
    root, l, r = map(str, input().split())
    ROOT = ord(root)-65
    L = ord(l)-65
    R = ord(r)-65
    if L >= 0:
        tree[ROOT].append(L)
    else:
        tree[ROOT].append(-1)
    if R >= 0:
        tree[ROOT].append(R)
    else:
        tree[ROOT].append(-1)

def preorder(root):
    if root != -1:
        print(chr(root+65), end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != -1:
        inorder(tree[root][0])
        print(chr(root+65), end='')
        inorder(tree[root][1])

def postorder(root):
    if root != -1:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(chr(root+65), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)