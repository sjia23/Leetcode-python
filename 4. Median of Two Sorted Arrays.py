class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)
        middle = (m + n) // 2
        nums3 = nums1 + nums2

        if (m + n) % 2 == 0:
            return (nums3[middle] + nums3[middle + 1]) / 2

        else:
            return nums3[middle + 1]


if __name__ == "__main__":
    s = Solution()
    s.findMedianSortedArrays(2, 3)
