#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    二倍数对数组
"""
import collections
from typing import List


"""
    先统计数据的绝对值的频数，然后将key值进行排序，查看前一个值的二倍在hash表中出现
"""
class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        d_dict = {}
        for x in A:
            x = abs(x)
            d_dict.setdefault(x, 0)
            d_dict[x] += 1

        key = list(d_dict.keys())
        key.sort()
        for x in key:
            if not d_dict[x]:
                continue

            if d_dict.get(x << 1, 0) >= d_dict[x]:
                d_dict[x << 1] -= d_dict[x]
            else:
                return False

        return True


# 简洁一些
class Solution2:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d_dict = collections.Counter(A)
        for x in sorted(d_dict, key=abs):
            if d_dict[x<<1] < d_dict[x]:
                return False
            d_dict[x<<1] -= d_dict[x]
        return True