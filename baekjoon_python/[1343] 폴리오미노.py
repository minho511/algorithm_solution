#2021 07 07 그리디
s = input()
answer = s.replace("XXXX","AAAA").replace("XX","BB")
if "X" in answer:
    print(-1)
else:
    print(answer)