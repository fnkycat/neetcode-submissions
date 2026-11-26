from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = 1

        while left <= right:
            k = (right + left) // 2
            wasted_time = 0
            for p in piles:
                wasted_time += ceil(p / k)
            if wasted_time <= h:
                result = k
                right = k - 1
            else:
                left = k + 1

        return result

