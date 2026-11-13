from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = dict(Counter(nums))
        
        for item, count in result.items():
            if count == 1:
                return item

        return None