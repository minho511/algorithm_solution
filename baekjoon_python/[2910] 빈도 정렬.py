# 2021 07 10 구현 자료 구조 정렬 트리를 사용한 집합과 맵
# https://www.acmicpc.net/problem/2910
import sys;input = sys.stdin.readline

def setting(data):
    return data[0]

n, c = map(int, input().split())
entered = list(map(int, input().split()))
array = []
find = []
for i in entered:
    if i not in find:  # 중복되는 수를 제외하기 위해 find리스트 사용
        find.append(i)
        array.append((entered.count(i),i))
# 같은 횟수로 나온 수에 대해서는 나온 순서를 고려해야 한다.
# 따라서 빈도에 대해서만 내림차순으로 정렬한다.
array.sort(reverse=True, key=setting)
for i in array:
    print(f"{i[1]} "*i[0],end="")

