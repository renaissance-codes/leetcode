#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    按奇偶排序数组
"""
from typing import List


# 替换左右的奇偶数 116ms
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1

        while i < j:
            while i < len(A) and A[i] % 2 == 0:
                i += 1
            while j >= 0 and A[j] % 2 == 1:
                j -= 1

            if i == len(A) or j < 0 or i >= j:
                break

            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A
