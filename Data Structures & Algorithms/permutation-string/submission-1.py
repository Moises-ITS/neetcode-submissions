class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s2 = [0] * 26
        count_s1 = [0] * 26
        matches = 0
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            matches += (1 if count_s1[i] == count_s2[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            #matches
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a') #number place on list
            #subtract s2[l] by 1
            #checking to see if s1[r] == s2[r] then + 1 matches

            count_s2[index] += 1 #increase s2[r] here aka increasing the windows
            if count_s1[index] == count_s2[index]:
                matches += 1
            elif count_s1[index] + 1 == count_s2[index]:
                matches -= 1
            
            lef = ord(s2[l]) - ord('a')
            count_s2[lef] -= 1
            if count_s1[lef] == count_s2[lef]:
                matches += 1
            elif count_s1[lef] - 1 == count_s2[lef]:
                matches -= 1
            l+=1
        return matches == 26
            






            

