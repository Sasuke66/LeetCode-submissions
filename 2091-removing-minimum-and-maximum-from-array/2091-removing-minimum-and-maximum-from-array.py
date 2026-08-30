class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        low, high = min(i, j), max(i, j)
        front = high + 1
        back = n - low
        front_back = (low + 1) + (n - high)
        return min(front, back, front_back)