from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        re = 0
        tmp = 0
        while l < r:
            if height[l] > height[r]:
                # re = max(re, height[r] * (r - l))
                tmp = height[r] * (r - l)
                re = max(re, tmp)
                r = r - 1

            elif height[l] <= height[r]:
                tmp = height[l] * (r - l)
                re = max(re, tmp)
                l = l + 1

        return re
