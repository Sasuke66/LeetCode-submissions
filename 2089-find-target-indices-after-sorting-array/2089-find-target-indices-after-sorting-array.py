class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] == target:
                l.append(i)
        return l