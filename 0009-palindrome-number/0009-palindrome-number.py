class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = int(str(abs(x))[::-1])
        if x == strX:
            return True
        else:
            return False