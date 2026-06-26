class Solution:
    def isPalindrome(self, s: str) -> bool:
                strins = "".join(char.lower() for char in s if char.isalnum())
                return strins == strins[::-1]