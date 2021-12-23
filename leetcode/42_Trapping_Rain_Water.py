# 2021 12 23 문자열
# https://leetcode.com/problems/trapping-rain-water/submissions/
# Runtime: 60 ms, faster than 98.77% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.5 MB, less than 96.63% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        m_idx = height.index(max(height))

        def cal_water(bars):
            m = 0
            result = 0
            for i in range(len(bars)):
                if bars[i] > m:
                    m = bars[i]
                else:
                    result += m - bars[i]
            return result

        forward = height[:m_idx + 1]
        backward = height[m_idx:]
        backward.reverse()
        answer = cal_water(forward) + cal_water(backward)
        return answer