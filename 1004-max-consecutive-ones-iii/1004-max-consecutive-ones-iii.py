class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = b = 0
        while b < len(nums):
            if nums[b] == 0:
                k -= 1
            b += 1
            if k < 0:
                if nums[a] == 0:
                    k += 1
                a += 1
        return b - a