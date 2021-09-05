def solution(new_id):
    # step1
    new_id = new_id.lower()
    # step2
    answer = ""
    remo = ['-','_','.']
    for c in new_id:
        if c.isdigit() or c.isalpha() or c in remo:
            answer+=c
    # step3
    while '..' in answer:
        answer = answer.replace('..','.')
    # step4
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer)>=1 and answer[-1] == '.':
        answer = answer[:-1]
    # step5
    if answer == '':
        answer='a'
    # step6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #step 7
    if len(answer) <= 2:
        k = answer[-1]
        while len(answer) < 3:
            answer+=k
    return answer