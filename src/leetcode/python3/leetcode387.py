#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    找出第一个重复的字母的索引
"""

# 先计算字母的频数，然后筛选出频数为1的首次索引
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for x in s:
            d.setdefault(x, 0)
            d[x] += 1

        for i, x in enumerate(s):
            if d[x] == 1:
                return i
        return -1