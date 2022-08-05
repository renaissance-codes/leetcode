#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    比特位计数
"""
from typing import List


# 利用规律来做 112ms
class Solution:
    def countBits(self, num: int) -> List[int]:

        res = [0] * (num + 1)
        if num == 0:
            return res
        ind = 0
        bit = 1
        while ind <= num:

            for i in range(bit):
                if ind + i + 1 <= num:
                    res[ind + i + 1] = res[i] + 1
                else:
                    break
            ind += bit
            bit <<= 1
        return res
