class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_count = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            max_count = max(max_count, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_count