class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        curr_height = 0
        for i in gain:
            curr_height += i
            max_height = max(max_height, curr_height)

        return max_height 