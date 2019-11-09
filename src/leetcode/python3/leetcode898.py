#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    子数组按位或操作
"""
from typing import List


# 动态规划
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set()
        tres = set()
        last = -1
        for x in A:
            if x == last:
                continue
            last = x
            ntres = set()
            for y in tres:
                ntres.add(y | x)
            ntres.add(x)

            res |= ntres
            tres = ntres
        return len(res)