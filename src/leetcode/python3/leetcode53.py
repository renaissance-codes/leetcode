#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

"""
  最大子序列和
"""


# 线性 96ms
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cal = nums[0]
        max_v = nums[0]
        for x in nums[1:]:
            if cal < 0:
                cal = x
            else:
                cal += x
            if cal > max_v:
                max_v = cal
        return max_v
