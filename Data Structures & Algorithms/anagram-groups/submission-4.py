class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            count = [0] * 26
            for let in word:
                count[ord(let) - ord('a')] += 1
            hashMap[tuple(count)] = hashMap.get(tuple(count), []) + [word]
        return list(hashMap.values())