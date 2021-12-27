# 2021 12 27 배열
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# Runtime: 1016 ms, faster than 69.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.4 MB, less than 5.23% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        candy = [0]
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                if prices[i] > buy:
                    candy.append(prices[i]-buy)
        return max(candy)

# 최대 이익과 최소 매입 가격을 한번에 갱신
# O(n)으로 풀이