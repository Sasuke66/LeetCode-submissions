class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        s = set()
        for i in range(n):
            if digits[i] % 2 == 0:
                for j in range(n):
                    if j != i and digits[j] != 0:
                        for k in range(n):
                            if j != k and k != i:
                                s.add(digits[j] * 100 + digits[k] * 10 + digits[i])
        return len(s)