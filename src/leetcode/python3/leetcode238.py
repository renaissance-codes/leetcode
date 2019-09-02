#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    除自身以外数组的乘积
"""
from typing import List


# 左右相乘
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]

        d_len = len(nums)
        left = 1
        right = 1
        for i in range(d_len):
            result[i] *= left
            left *= nums[i]

            result[d_len - i - 1] *= right
            right *= nums[d_len - i - 1]

        return result
