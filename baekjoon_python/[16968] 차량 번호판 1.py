# 2021 07 28 수학 조합론
# https://www.acmicpc.net/problem/16968
s = input()
if len(s) == 1:
    if s == 'd':
        print(10)
    elif s == 'c':
        print(26)
elif len(s) == 2:
    if s == 'dd':
        print(90)
    elif s == 'dc' or s == 'cd':
        print(260)
    elif s == 'cc':
        print(650)
elif len(s) == 3:
    if s == 'ddd':
        print(810)
    elif s == 'ddc'or s == 'cdd':
        print(2340)
    elif s == 'dcd':
        print(2600)
    elif s == 'dcc'or s=='ccd':
        print(6500)
    elif s == 'cdc':
        print(6760)
    elif s == 'ccc':
        print(16250)
else:
    if s == 'dddd':
        print(7290)
    elif s == 'dddc'or s== 'cddd':
        print(21060)
    elif s == 'dcdd' or s == 'ddcd':
        print(23400)
    elif s == 'ddcc' or s=='ccdd':
        print(58500)
    elif s == 'dcdc' or s=='cdcd':
        print(67600)
    elif s == 'dccd':
        print(65000)
    elif s == 'cddc':
        print(60840)
    elif s == 'dccc'or s =='cccd':
        print(162500)
    elif s == 'cdcc' or s == 'ccdc':
        print(169000)
    elif s == 'cccc':
        print(406250)





