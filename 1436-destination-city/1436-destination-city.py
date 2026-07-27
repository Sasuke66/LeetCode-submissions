class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ends = {end for end, in_ in paths}
        for end, in_ in paths:
            if in_ not in ends:
                return in_