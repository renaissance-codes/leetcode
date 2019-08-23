#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    范围求和II
"""
from typing import List

# 直观思路 108ms
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n
        for op in ops:
            min_m = min(op[0], min_m)
            min_n = min(op[1], min_n)
        return min_m * min_n


# 104ms
class Solution2:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n
        for op in ops:
            min_m = min(op[0], min_m)
            min_n = min(op[1], min_n)

            if min_m == 1 and min_n == 1:
                break
        return min_m * min_n