class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for c in costs:
            count[c] += 1
        icbars = 0
        for c in range(1, min(max_cost, coins) + 1):
            buy = min(count[c], coins//c)
            coins -= c * buy
            icbars += buy
        return icbars