#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    排序数组
"""
from typing import List


# 使用计数排序 208ms
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_v = min(nums)
        max_v = max(nums)
        key = [0 for i in range(max_v - min_v + 1)]
        for n in nums:
            key[n - min_v] += 1

        result = []
        for i, k in enumerate(key):
            if k:
                result += [i + min_v] * k
        return result