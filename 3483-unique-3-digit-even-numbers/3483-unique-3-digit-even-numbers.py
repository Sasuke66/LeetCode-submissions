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
                                s.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(s)