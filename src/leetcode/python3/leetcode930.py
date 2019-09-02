#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    和相同的二元子数组
"""
from typing import List


# 前缀数组
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        d_dict = {0: 1}

        last = 0
        ans = 0
        for x in A:
            last += x
            if last - S in d_dict:
                ans += d_dict[last - S]

            d_dict.setdefault(last, 0)
            d_dict[last] += 1

        return ans


# 统计连续0的个数
class Solution2:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        ans = 0
        front = 0
        loc = []
        for x in A:
            if x == 0:
                front += 1
            else:
                loc.append(front)
                front = 0
        loc.append(front)

        for i in range(len(loc) - S):
            if S == 0:
                ans += ((loc[i] + 1) * loc[i]) >> 1
            else:
                ans += (loc[i] + 1) * (loc[i + S] + 1)
        return ans
