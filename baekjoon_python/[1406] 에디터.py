# 자료 구조 스택 연결리스트
# https://www.acmicpc.net/problem/1406
import sys; input = sys.stdin.readline


forw = list(input()[:-1])
back = []

for _ in range(int(input())):
    comm = input()[:-1]
    if comm[0] == 'P':
        forw.append(comm[2])
    elif comm == 'L' and forw:
        back.append(forw.pop())
    elif comm == 'D' and back:
        forw.append(back.pop())
    elif comm == 'B' and forw:
        forw.pop()
    
print("".join(forw+back[::-1]))

# 시간 초과
# sen = list(input())
# cursor = len(sen)
# for i in range(int(input())):
#     comm = input()
#     # comm P
#     if comm[0] == 'P':
#         sen.insert(cursor, comm[2])
#         cursor += 1
#     # comm L D B
#     elif comm == 'L' and cursor != 0:
#         cursor -= 1
#     elif comm == 'D'and cursor < len(sen):
#         cursor += 1 
#     elif comm == 'B' and cursor > 0:
#         sen.pop(cursor-1)
#         cursor -= 1
# print("".join(sen))