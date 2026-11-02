class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in brackets_dict:
                if stack and stack[-1] == brackets_dict.get(char):
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return not stack