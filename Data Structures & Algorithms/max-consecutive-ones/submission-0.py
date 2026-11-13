class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, profit = 0, 0

        for n in nums:
            if n == 1:
                count += 1
                profit = max(profit, count)

            else:
                count = 0

        return profit