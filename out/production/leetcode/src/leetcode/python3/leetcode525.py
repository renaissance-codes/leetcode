#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    最长子数组
"""
from typing import List

#  暴力破解，由于时间限制，不能通过
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            if (len(nums) - i) < max_len:
                break
            for j in range(i + 1, len(nums), 2):
                if sum(nums[i:j + 1]) * 2 == (j + 1 - i) and j - i + 1 > max_len:
                    max_len = j - i + 1

        return max_len

# 增加了索引机制，可以通过测试1192ms
class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        d = {0: -1}
        tv = 0
        for i, x in enumerate(nums):
            if x:
                tv += 1
            else:
                tv -= 1

            if tv not in d:
                d[tv] = i
            else:
                if max_len < i - d[tv]:
                    max_len = i - d[tv]

        return max_len
