class Solution:
    def isPalindrome(self, s: str) -> bool:
        format_s = "".join(char for char in s if char.isalnum()).lower()
        return format_s == format_s[::-1]