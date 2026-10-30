class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums[i + 1:]:
                index = nums[i + 1:].index(result) + (i + 1)
                answer += i, index

        return answer