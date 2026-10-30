class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = True
        flag = False if len(nums) == len(set(nums)) else True

        return flag