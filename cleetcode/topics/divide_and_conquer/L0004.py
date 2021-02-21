from cleetcode.ctest import cL0004

from typing import List


class Solution:
    __doc__ = cL0004.__ctest__

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        len1, len2 = len(nums1), len(nums2)

        low = 0
        high = len2

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1

            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == len1 else nums1[partition1]

            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == len2 else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len1 + len2) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()

