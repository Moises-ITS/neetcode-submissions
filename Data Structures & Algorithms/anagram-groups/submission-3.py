class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #ord
        hashMap = {}
        for word in strs:
            counter = [0] * 26
            for let in word:
                counter[ord(let) - ord("a")] += 1
            hashMap[tuple(counter)] = hashMap.get(tuple(counter), []) + [word]
        
        return list(hashMap.values())