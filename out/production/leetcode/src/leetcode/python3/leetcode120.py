#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    三角形最小路径
"""

from typing import List


# 动态规划，维特比算法
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        d_len = len(triangle)
        if d_len == 0:
            return 0
        path = [0 for i in range(d_len)]

        for num, tri in enumerate(triangle):
            for i in range(num, -1, -1):
                if i == 0:
                    path[i] = path[i] + tri[i]
                elif i == num:
                    path[i] = path[i - 1] + tri[i]
                else:
                    path[i] = min(path[i], path[i - 1]) + tri[i]
        return min(path)