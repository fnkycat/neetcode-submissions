class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                triplets = a + nums[left] + nums[right]
                if triplets > 0:
                    right -= 1
                elif triplets < 0:
                    left += 1
                else:
                    answer.append([a, nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
        return answer

