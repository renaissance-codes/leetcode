#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    回文数
"""


# 转化为字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        xs = str(x)
        xlen = len(xs)

        i = 0
        j = xlen - 1
        while i < j:
            if xs[i] != xs[j]:
                return False
            i += 1
            j -= 1


# 比较位数逆转数字是否相同
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        t = 0
        nx = x
        while nx:
            t = t * 10 + nx % 10
            nx //= 10

        return t == x
