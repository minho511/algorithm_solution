# 2021 6 28 백준 10828
import sys
input = sys.stdin.readline

stack = []

n = int(input())

for i in range(n):
    ent = input()
    if ent[:4] == "push":
        stack.append(int(ent[5:]))
    elif ent == "pop\n":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ent == "size\n":
        print(len(stack))
    elif ent == "empty\n":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ent == "top\n":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
