#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    得分最高的最小轮调
"""
from typing import List


# 寻找规律
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        a_len = len(A)
        res = [0] * a_len

        for i, x in enumerate(A):
            k = (i - x + a_len + 1) % a_len
            res[k] += 1

        ae = 0
        ar = res[0]
        for i in range(1, a_len):
            res[i] += res[i - 1] - 1

            if res[i] < ar:
                ar = res[i]
                ae = i
        return ae
