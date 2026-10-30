from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s, char_count_t = Counter(list(s)), Counter(list(t))
        result = char_count_s == char_count_t

        return result