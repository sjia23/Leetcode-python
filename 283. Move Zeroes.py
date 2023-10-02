from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return 0
        j = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    ans = s.moveZeroes(nums)
    print(ans)
