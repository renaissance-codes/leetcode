#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    数组拆分
"""
from typing import List

# 先排序
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        d_len = len(nums)
        nums.sort()
        max_v = 0
        for i in range(d_len // 2):
            max_v += nums[2 * i]

        return max_v