#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    子集II
"""
from typing import List


# 累积算法，注意重复的元素
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = [[]]
        add = None
        last = None
        nums.sort(reverse=True)

        for x in nums:
            nadd = []
            if x != last:
                for n in res:
                    nadd.append([x] + n)
            else:
                for n in add:
                    nadd.append([x] + n)

            res += nadd
            last = x
            add = nadd
        return res
