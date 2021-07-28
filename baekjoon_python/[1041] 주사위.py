# 2021 07 20 수학 그리디
# https://www.acmicpc.net/problem/1041
import sys; input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    # 5개 면 노출
    print(sum(nums) - max(nums))
    exit()
# A 0 B 1 C 2 D 3 E 4 F 5 마주보는 인덱스 합 5 따라서 모든 경우의 수에서 인덱스 합이 5가되는 경우가 있으면 그 경우를 제외
case2 = [(0,1),(0,2),(0,3),(0,4),(5,1),(5,2),(5,3),(5,4),(1,3),(1,2),(3,4),(4,2)]
case3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
case2_a = []
case3_a = []
for i in case2:
    case2_a.append(nums[i[0]] + nums[i[1]])
for i in case3:
    case3_a.append(nums[i[0]] + nums[i[1]] + nums[i[2]])
# 한개 면 노출
m1 = min(nums) * (5*(n**2)-16*n+12)
# 두개 면 노출
m2 = min(case2_a) * (8 * n - 12)
# 세개 면 노출
m3 = min(case3_a) * 4
print(m1+m2+m3)