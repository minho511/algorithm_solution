# 2021 08 17 정렬 level1
# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for com in commands :
        array2 = sorted(array[com[0]-1:com[1]])
        num = array2[com[2]-1]
        answer.append(num)
    return answer