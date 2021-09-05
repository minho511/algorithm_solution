def solution(record):
    answer = []
    dict = {}
    a = []
    for data in record:
        t = list(map(str, data.split()))
        if t[0] == 'Enter':
            dict[t[1]] = t[2]
            a.append((1, t[1]))
        elif t[0] == 'Change':
            dict[t[1]] = t[2]
    for data in a:
        if data[0] == 1:
            answer.append("{}님이 들어왔습니다.".format(dict[data[1]]))
        elif data[0] == 0:
            answer.append("{}님이 나갔습니다.".format(dict[data[1]]))
    return answer