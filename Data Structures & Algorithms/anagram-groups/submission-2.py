from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #ord = [0] * 26
        hashMap = defaultdict(list)
        for word in strs:
            constant = [0] * 26
            for let in word:
                constant[ord(let) - ord('a')] += 1
            hashMap[tuple(constant)] += ([word])
        return list(hashMap.values())