class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for word in strs:
            count = [0] * 26
            for let in word:
                count[ord(let)-ord('a')] += 1
            mp[tuple(count)] = mp.get(tuple(count), []) + [word]
        
        return list(mp.values())