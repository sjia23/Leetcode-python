from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, l, r = 0, 0, len(nums) -1
        while r > l:
            x = nums[l] + nums[r]
            if x > k:
                r -= 1
            elif x < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [3,1,3,4,3]
    k = 6
    ans = s.maxOperations(nums, k)
    print(ans)