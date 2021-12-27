# 2021 12 27 배열
# https://leetcode.com/problems/product-of-array-except-self/submissions/
# Runtime: 244 ms, faster than 54.30% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.6 MB, less than 7.91% of Python3 online submissions for Product of Array Except Self.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1]
        r2l = [1]
        nl, nr  = 1, 1
        for i in range(len(nums)-1):
            nl *= nums[i]
            nr *= nums[len(nums)-i-1]
            l2r.append(nl)
            r2l.append(nr)
        r2l.reverse()
        result = [l2r[i] * r2l[i] for i in range(len(nums))]
        return result

# 나눗셈을 하지 않고 O(n)에 풀이하라는 조건이 있었다.
# 1. 왼쪽 부터 곱셈한 결과와 오른쪽 부터 곱셈한 결과를 두 리스트에 저장한다.
# 2. 두 리스트는 처음에 1을 기본적으로 가지고 있는다. (이는 마지막 연산을 간편하게 해준다.)
# 3. 오른쪽에서 왼쪽으로 계산한 결과를 저장하는 리스트는 역순으로 재배열 해준다.
# 4. 두 리스트의 같은 인덱스에 위차한 수를 곱한다.