#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    倒排数字，数字是4个字节有符号的整数，如果倒排的数字超过范围则为0
"""


# 非常朴素的思路,40ms
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        sign = 1
        reverse = 0
        if x < 0:
            sign = -1
            x = -x
        while x:
            reverse = reverse * 10 + x % 10
            x //= 10
        if sign == 1:
            if reverse > (1<<31)-1:
                return 0
        else:
            if reverse > 1<<31:
                return 0
        return sign * reverse