#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    表现良好的最长时间段
"""
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hsum = [0]
        for h in hours:
            v = -1
            if h > 8:
                v = 1
            hsum.append(v + hsum[-1])
        maxv = 0
        minv = len(hours)
        dlist = []

        for i, x in enumerate(hsum):
            if x < minv:
                minv = x
                dlist.append((x, i))
            else:
                for xv, xi in dlist:
                    if x > xv:
                        maxv = max(maxv, i - xi)
                        break
        return maxv


# 前缀数组和+单调栈
class Solution2:
    def longestWPI(self, hours: List[int]) -> int:
        hsum = [0]
        for h in hours:
            v = -1
            if h > 8:
                v = 1
            hsum.append(v + hsum[-1])
        minv = len(hours)
        dlist = []

        for i, x in enumerate(hsum):
            if x < minv:
                minv = x
                dlist.append((x, i))
        i = len(hsum) - 1
        ans = 0
        while i > ans:
            while dlist and dlist[-1][0] < hsum[i]:
                ans = max(ans, i - dlist[-1][1])
                dlist.pop()
            i -= 1
        return ans