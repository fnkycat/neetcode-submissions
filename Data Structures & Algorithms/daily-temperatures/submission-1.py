class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                old_day = stack.pop()
                result[old_day] = i - old_day

            stack.append(i)

        return result