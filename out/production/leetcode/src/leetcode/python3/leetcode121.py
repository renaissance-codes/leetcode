#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    买卖股票的最佳时机
"""
from typing import List

# O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_v = float("inf")
        for x in prices:
            if x < min_v:
                min_v = x
            elif x - min_v > profit:
                profit = x - min_v

        return profit
