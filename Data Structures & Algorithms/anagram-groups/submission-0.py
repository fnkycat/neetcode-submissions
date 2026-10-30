from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams_dict:
                anagrams_dict[key] = []
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())

