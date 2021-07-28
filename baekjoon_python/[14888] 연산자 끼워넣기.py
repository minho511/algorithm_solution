# 2021 07 25 브루트포스 백트래킹
# https://www.acmicpc.net/problem/14888
import sys; input = sys.stdin.readline
from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
a = list(map(int, input().split()))
oper = ['+']*a[0] + ['-']*a[1] + ['*']*a[2] + ['//']*a[3]
c = permutations(oper,n-1)
_min = int(1e9)
_max = -int(1e9)
for i in c:
    res = nums[0]
    for j in range(1,n):
        if i[j-1] == '//':
            if res<0:
                res = -1*(-res//nums[j])
            else:
                res //= nums[j]
        elif i[j-1] == '+':
            res += nums[j]
        elif i[j-1] == '-':
            res -= nums[j]
        elif i[j-1] == '*':
            res *= nums[j]
    if res>_max:
        _max = res
    if res<_min:
        _min = res
print(_max)
print(_min)

#import sys
input = sys.stdin.readline

N = int( input() )
nums = list( map( int, input().split() ) )
oper = list( map( int, input().split() ) )

# 참고 : 1등 코드 https://www.acmicpc.net/source/18588482
# method 2
#import sys
# input = sys.stdin.readline
#
# N = int( input() )
# nums = list( map( int, input().split() ) )
# oper = list( map( int, input().split() ) )
# def backtrack( prevVal, size, idx, plus, minus, multi, divide ):
# 	global max, min
# 	if size == N - 1:
# 		if max < prevVal:
# 			max = prevVal
# 		if min > prevVal:
# 			min = prevVal
# 	else:
# 		if plus:
# 			backtrack( prevVal + nums[idx], size + 1, idx + 1, plus - 1, minus, multi, divide )
#
# 		if minus:
# 			backtrack( prevVal - nums[idx], size + 1, idx + 1, plus, minus - 1, multi, divide )
#
# 		if multi:
# 			backtrack( prevVal * nums[idx], size + 1, idx + 1, plus, minus, multi - 1, divide )
#
# 		if divide:
# 			if prevVal < 0:
# 				backtrack( -(abs(prevVal) // nums[idx]), size + 1, idx + 1, plus, minus, multi, divide - 1 )
# 			else:
# 				backtrack( prevVal // nums[idx], size + 1, idx + 1, plus, minus, multi, divide - 1 )
# max = -(10**9+1)
# min = 10 ** 9 + 1
# backtrack( nums[0], 0, 1, *oper )
# print( max, min, sep = '\n' )