#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    山脉数组中查找目标值
"""

# 先找山顶，在二分查找
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        i = 0
        d = mountain_arr.length() - 1

        def search(start, end):
            if start == end:
                return start
            mid = (start + end) >> 1
            mid_v = mountain_arr.get(mid)
            right_v = mountain_arr.get(mid + 1)
            if mid == start:
                if mid_v > right_v:
                    return mid
                else:
                    return end
            left_v = mountain_arr.get(mid - 1)
            if mid_v < left_v:
                return search(start, mid - 1)
            elif mid_v < right_v:
                return search(mid + 1, end)
            else:
                return mid

        def s1(start, end):
            if start > end:
                return -1
            mid = (start + end) >> 1
            mid_v = mountain_arr.get(mid)
            if mid_v > target:
                return s1(start, mid - 1)
            elif mid_v < target:
                return s1(mid + 1, end)
            else:
                return mid

        def s2(start, end):
            if start > end:
                return -1
            mid = (start + end) >> 1
            mid_v = mountain_arr.get(mid)
            if mid_v > target:
                return s2(mid + 1, end)
            elif mid_v < target:
                return s2(start, mid - 1)
            else:
                return mid

        s_index = search(0, d)

        s1_index = s1(0, s_index)
        if s1_index != -1:
            return s1_index
        return s2(s_index, d)
