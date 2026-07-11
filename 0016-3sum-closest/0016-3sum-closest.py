class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = nums[0] + nums[1] + nums[2], len(nums)
        for i in range(n):
            comp, j, k = target - nums[i], i + 1, n - 1
            while j < k:
                curr = nums[j] + nums[k] + nums[i]
                if abs(curr - target) < abs(ans - target):
                    ans = curr
                if nums[j] + nums[k] == comp:
                    return ans
                elif nums[j] + nums[k] > comp:
                    k -= 1
                else:
                    j += 1
        return ans
        # closest = nums[0] + nums[1] + nums[2]
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if abs(target - (nums[i] + nums[j] + nums[k]))< abs(target-closest):
        #                 closest = nums[i] + nums[j] + nums[k]
        # return closest
