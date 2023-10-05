from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum = 0
        for i in range(k):
            cursum += nums[i]
        maxsum = cursum
        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i - k]
            maxsum = max(cursum, maxsum)
        return maxsum / k
