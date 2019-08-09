#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    倒排数字，数字是4个字节有符号的整数，如果倒排的数字超过范围则为0
"""

from functools import reduce

# 非常朴素的思路
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        d = []
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x:
            t = x % 10
            d.append(t)
            x //= 10
        r = reduce(lambda x, y: x * 10 + y, d)
        if sign == 1:
            if r > (1 << 31) - 1:
                return 0
        else:
            if r > 1 << 31:
                return 0
        return sign * r
