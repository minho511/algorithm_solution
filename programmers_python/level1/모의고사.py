# 2021 08 17 완전탐색 level1
# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    l = len(answers)
    supo = [
          [1, 2, 3, 4, 5]*(l//5+1),
          [2, 1, 2, 3, 2, 4, 2, 5]*(l//8+1),
          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(l//10+1)]
    cnt = [0,0,0]
    for i in range(l):
        for j in range(3):
            if supo[j][i] == answers[i]:
                cnt[j]+=1
    mx = max(cnt)
    answer =[]
    for index, count in enumerate(cnt):
        if count == mx:
            answer.append(index+1)
    return answer