class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        answer = []

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                answer += [left+1, right+1]
                break
            elif s < target:
                left += 1
            else:
                right -= 1

        return answer