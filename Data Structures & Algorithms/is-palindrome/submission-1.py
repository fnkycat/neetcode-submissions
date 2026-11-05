import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        fix = str.maketrans('', '', string.punctuation + ' ')
        result = s.translate(fix).lower()
        flag = True

        left, right = 0, len(result) - 1
        while left < right:
            if result[left] != result[right]:
                flag = False
                break
            left += 1
            right -= 1

        return flag
        