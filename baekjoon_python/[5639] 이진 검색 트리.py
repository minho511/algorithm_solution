# 2021 08 10 그래프 이론 그래프 탐색 트리 너비 우선 탐색 깊이 우선 탐색
# https://www.acmicpc.net/problem/11725
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_search_tree(start, end):
    if start > end:
        return
    root = array[start]
    i = start+1
    while i <=end:
        if array[i] > root:
            break
        i+=1
    binary_search_tree(start+1, i-1)
    binary_search_tree(i, end)
    sys.stdout.write('{}\n'.format(root))

array = []
while True:
    try:
        array.append(int(input()))
    except:
        break
binary_search_tree(0, len(array)-1)