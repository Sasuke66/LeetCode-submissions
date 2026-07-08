class Solution:
    def repeatedCharacter(self, s: str) -> str:
        twiceletters = []
        for t in s:
            if t in twiceletters:
                return t
            else:
                twiceletters.append(t)