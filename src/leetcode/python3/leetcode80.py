#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    删除排序数组中的重复项
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        i = 0
        j = 1
        d_len = len(nums)

        while j < d_len:

            if nums[j] != nums[i]:
                count = 1
                i += 1
                nums[i] = nums[j]
            elif count < 2:
                count += 1
                i += 1
                nums[i] = nums[j]

            j += 1

        return i + 1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        d_len = len(nums)
        if d_len < 3:
            return d_len
        i = 1

        for j in range(2, d_len):

            if nums[i - 1] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
