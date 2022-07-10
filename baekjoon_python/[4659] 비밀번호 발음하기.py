# 구현 문자열
# https://www.acmicpc.net/problem/4659
#import sys; input=sys.stdin.readline().rstrip
mo = ['a','e','i','o','u']
    
while True:
    s = input()
    if s == 'end':
        break
    pre = '!'
    code = []
    con1 = False
    for c in s:
        if pre == c:
            if pre != 'e' and pre !='o':
                con1 = True
                break
        if c in mo:
            code.append(1)
        else:
            code.append(0)
        pre = c
    if con1:
        print(f"<{s}> is not acceptable.")
        continue
    if sum(code) == 0:
        print(f"<{s}> is not acceptable.")
        continue
    # ex ptoui -> code = [0,0,1,1,1]
    con2 = False
    for i in range(2,len(code)):
        if code[i-2:i+1] == [0,0,0] or code[i-2:i+1]== [1,1,1]:
            con2 = True
            break
    if con2:
        print(f"<{s}> is not acceptable.")
        continue
    print(f"<{s}> is acceptable.")