#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    零钱兑换II
"""
from typing import List


# 动态规划
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        ddict = []
        coins.sort()
        for x in range(1, amount + 1):
            d = [0] * len(coins)
            for i, c in enumerate(coins):
                if c > x:
                    d[i] = d[i - 1]
                elif c == x:
                    d[i] = 1 + d[i - 1]
                else:
                    d[i] = ddict[x - c - 1][i] + d[i - 1]

            ddict.append(d)
        return ddict[-1][-1]


# 一维数组
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        ddict = [0] * (amount + 1)
        dcoin = len(coins)
        ddict[0] = 1
        # coins.sort()
        for c in coins:
            for x in range(1, amount + 1):
                if x >= c:
                    ddict[x] = ddict[x - c] + ddict[x]
        return ddict[-1]

