#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    旋转函数
"""
from typing import List


# 利用公式进行处理
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        sum_a = 0
        start = 0
        for i, a in enumerate(A):
            sum_a += a
            start += i * a
        max_a = start
        max_d = len(A)
        for i, x in enumerate(A[:-1]):
            v = start - sum_a + max_d * A[i]
            max_a = max(v, max_a)
            start = v

        return max_a