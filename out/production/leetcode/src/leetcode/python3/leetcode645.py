#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    找出错误数字以及原本数字
"""
from typing import List


# 暴力解法 288ms
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = set()
        repeat = -1
        sum_d = (1 + len(nums)) * len(nums) // 2
        for x in nums:
            if x in d:
                repeat = x
            else:
                d.add(x)
            sum_d -= x

        return [repeat, sum_d + repeat]