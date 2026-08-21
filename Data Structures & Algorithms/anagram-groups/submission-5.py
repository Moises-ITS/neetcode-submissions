class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            count = [0] * 26
            for let in word:
                count[ord(let) - ord('a')] += 1
            seen[tuple(count)] = seen.get(tuple(count), []) + [word]
        return list(seen.values())