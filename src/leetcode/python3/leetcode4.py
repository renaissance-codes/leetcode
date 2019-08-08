#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    这道题简单来讲就是从两个有序的数组中寻找中位数,要求时间复杂度为log(m+n) 2019/08/06
"""
from typing import List


# 1 简单思路, 速度 144ms, 没有达到标准，虽然可以通过测试
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self.getMedian(nums2)
        if len(nums2) == 0:
            return self.getMedian(nums1)
        if nums1[-1] <= nums2[0]:
            return self.getMedian(nums1 + nums2)
        if nums2[-1] <= nums1[0]:
            return self.getMedian(nums2 + nums1)
        k = len(nums1) + len(nums2)
        media = k // 2
        i1 = 0
        i2 = 0
        i = 0
        q = []
        while i < media + 1:
            if len(nums1) == i1:
                q.append(nums2[i2])
                i2 += 1
            elif len(nums2) == i2:
                q.append(nums1[i1])
                i1 += 1
            else:
                if nums1[i1] < nums2[i2]:
                    q.append(nums1[i1])
                    i1 += 1
                else:
                    q.append(nums2[i2])
                    i2 += 1
            i += 1

        if k % 2:
            return q[-1]
        else:
            return (q[-1] + q[-2]) / 2

    def getMedian(self, nums: List[int]) -> float:
        if len(nums) % 2:
            return nums[len(nums) // 2] * 1.0
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2

# 2 二分法
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        imin = 0
        imax = m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if j != 0 and i != m and nums2[j - 1] > nums1[i]:
                imin += 1
            elif i != 0 and j != n and nums1[i - 1] > nums2[j]:
                imax -= 1
            else:
                max_left = 0
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2:
                    return max_left

                min_right = 0
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2


#  140ms 二分法，奇怪的是速度优势并不是很明显
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        imin = 0
        imax = m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if j != 0 and i != m and nums2[j - 1] > nums1[i]:
                imin += 1
            elif i != 0 and j != n and nums1[i - 1] > nums2[j]:
                imax -= 1
            else:
                max_left = 0
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2:
                    return max_left

                min_right = 0
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2


if __name__ == "__main__":
    pass
