#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    多边形三角剖分的最低得分
"""
from typing import List


# 动态规划
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        alen = len(A)
        cache = [[0 if j + 1 == i else float("inf") for i in range(alen)] for j in range(alen)]

        for i in range(2, alen):
            for j in range(alen - i):
                minv = cache[j][j + i]
                for k in range(j + 1, j + i):
                    minv = min(minv, cache[j][k] + cache[k][j + i] + A[j] * A[k] * A[j + i])
                cache[j][j + i] = minv
        return cache[0][alen - 1]
