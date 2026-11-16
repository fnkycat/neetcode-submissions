from itertools import combinations

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = iter(t)
        result = all(char in check for char in s)

        return result
