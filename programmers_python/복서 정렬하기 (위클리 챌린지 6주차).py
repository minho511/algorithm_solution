# 프로그래머스 위클리챌린지 6주차
# https://programmers.co.kr/learn/courses/30/lessons/85002
def solution(weights, head2head):
    n = len(weights)
    count = [0]*n  # 자신보다 몸무게가 무거운 복서를 이긴 횟수
    win = [0]*n  # 이긴 횟수
    fight = [0]*n  # 각 선수별 경기수
    answer = []
    for i in range(n):
        for j in range(i+1, n):
            if head2head[i][j] == 'W':
                fight[i] +=1
                fight[j] +=1
                win[i] += 1
                if weights[i] < weights[j]:
                    count[i]+=1
            elif head2head[i][j] == 'L':
                fight[i] +=1
                fight[j] +=1
                win[j] +=1
                if weights[j] < weights[i]:
                    count[j]+=1
    per = [0]*n  # 승률
    data = []
    for i in range(n):
        if fight[i] != 0:
            per[i] = win[i]/fight[i]
        data.append([-per[i], -count[i], -weights[i], i+1])
    data.sort()
    for i in range(n):
        answer.append(data[i][-1])
    return answer
