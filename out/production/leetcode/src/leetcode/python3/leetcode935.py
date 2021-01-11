#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    骑士拨号器
"""


# 自底向上 动态规划
class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10
        dmp = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
               5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        result = {k: 1 for k in range(10)}

        for x in range(1, N):
            nresult = {}
            for k, vlist in dmp.items():
                nv = 0
                for v in vlist:
                    nv += result[v]
                nresult[k] = nv
            result = nresult
        num = 0
        for _, v in result.items():
            num += v
        return num % (10 ** 9 + 7)