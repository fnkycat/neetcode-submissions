class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0

        for num in s:
            if (num - 1) not in s:
                current_num = num
                current_count = 1

                while (current_num + 1) in s:
                    current_num += 1
                    current_count += 1

                count = max(count, current_count)

        return count