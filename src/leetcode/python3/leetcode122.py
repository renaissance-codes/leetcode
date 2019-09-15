#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    买卖股票的最佳时机II
"""
from typing import List


# 低买高卖 92ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minv = float("inf")
        flag = 0
        cost = -1
        maxv = -1
        for x in prices:
            if flag == 0:
                if x <= minv:
                    minv = x
                else:
                    cost = minv
                    flag = 1
                    maxv = x
            else:
                if x >= maxv:
                    maxv = x

                else:
                    ans += (maxv - cost)
                    flag = 0
                    minv = x
        if flag == 1:
            ans += (maxv - cost)

        return ans


# 贪婪算法
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        last = float("inf")
        for x in prices:
            if x > last:
                ans += x-last
            last = x
        return ans
