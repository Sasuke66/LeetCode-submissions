class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for p in words:
            if p.startswith(pref):
                count += 1
        return count