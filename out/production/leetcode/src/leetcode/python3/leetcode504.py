#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    七进制数
"""


# 无脑写
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = 1
        if num < 0:
            sign = -1
            num = -num

        res = 0
        i = 0
        while num != 0:
            res += (num % 7) * (10 ** i)
            num //= 7
            i += 1
        return str(sign * res)
