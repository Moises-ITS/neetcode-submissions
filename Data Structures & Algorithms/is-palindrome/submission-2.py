class Solution:
    def isPalindrome(self, s: str) -> bool:
        bare = ''.join(j.lower() for j in s if j.isalnum())
        l = 0
        r = len(bare) - 1
        while l < r:
            if bare[l] != bare[r]:
                return False
            l += 1
            r -= 1
        return True
