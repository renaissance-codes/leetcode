#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    搜索旋转排序数组
"""
from typing import List


# 先寻找旋转点然后进行查询， 64ms
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1

        def find_cut(start, end):
            if start == end:
                return start
            mid = (start + end) >> 1
            if mid == start:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return -1

            elif mid == end:
                if nums[mid] < nums[mid - 1]:
                    return mid
                else:
                    return -1
            else:
                if nums[mid] >= nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                if nums[start] > nums[mid]:
                    end = mid
                else:
                    start = mid + 1
                return find_cut(start, end)

        mid_ind = find_cut(0, len(nums) - 1)

        def binary_search(start, end):
            if start > end:
                return -1
            mid = (start + end) >> 1
            real_mid = (mid + mid_ind + 1) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] > target:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)

        return binary_search(0, len(nums) - 1)


# 做好边界处理
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1
        def binary_find(start, end):
            if start > end:
                return -1
            mid = (start+end)>>1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                res = binary_find(start, mid-1)
                if res == -1 and nums[mid] >= nums[start]:
                    return binary_find(mid+1, end)
                else:
                    return res
            else:
                res = binary_find(mid+1, end)
                if res == -1 and nums[mid] < nums[start]:
                    return binary_find(start, mid)
                else:
                    return res
        return binary_find(0, len(nums)-1)
