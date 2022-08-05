#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    数组和数字之间的加法
"""
from typing import List


# 直观解法 388ms
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        p = 0
        result = A[::-1]
        i = 0
        while (K or p) and i < len(A):
            t = K % 10
            if result[i] + t + p >= 10:
                result[i] = result[i] + t + p - 10
                p = 1
            else:

                result[i] = result[i] + t + p
                p = 0
            i += 1
            K //= 10

        while p or K:
            t = K % 10
            if t + p >= 10:
                result.append(t + p - 10)
                p = 1
            else:
                result.append(t + p)
                p = 0
            K //= 10
        return result[::-1]

# 380ms
class Solution2:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = []
        while K:
            k, v = divmod(K, 10)

            s = A.pop() if len(A) else 0

            x, y = divmod(v + s, 10)

            result.append(y)
            K = k + x

        return A + result[::-1]