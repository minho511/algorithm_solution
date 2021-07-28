# 2021 07 26 구현 자료 구조 문자열 파싱 덱
# https://www.acmicpc.net/problem/5430
import sys; input = sys.stdin.readline
t = int(input())
for _ in range(t):
    _cmd = input()[:-1]
    n = int(input())
    s = input()[:-1]
    if n == 0:
        array = []
        check_error = False
        for i in _cmd:
            if i == 'D':
                check_error = True
                break
        if check_error:
            print("error")
        else:
            print("[]")
    else:
        array = list(map(int, s[1:-1].split(',')))
        cntR = 0
        std_index = 0
        check_error = False
        for i in _cmd:
            if i == 'D':
                if array:
                    array.pop(std_index)
                else:
                    check_error = True
                    break
            elif i == 'R':
                cntR += 1
                if cntR%2==1:
                    std_index = -1
                else:
                    std_index = 0
        if check_error:
            print("error")
        else:
            if cntR%2 == 1:
                print(str(array[::-1]).replace(' ',''))
            else:
                print(str(array).replace(' ',''))