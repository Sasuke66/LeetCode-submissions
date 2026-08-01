class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            by_3 = (i % 3 == 0)
            by_5 = (i % 5 == 0)
            if by_3 and by_5:
                s = "FizzBuzz"
            elif by_3:
                s = "Fizz"
            elif by_5:
                s = "Buzz"
            else:
                s = str(i)
            ans.append(s)
        return ans