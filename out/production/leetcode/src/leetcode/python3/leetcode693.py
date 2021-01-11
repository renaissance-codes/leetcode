#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    交替位二进制数
"""


# 使用位运算
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        t = 0
        nx = n
        while nx:
            t += 1
            nx >>= 1
        v = (n>>1)^n
        if (n>>1)^n == (1<<t)-1:
            return True
        return False

#  40ms
class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        t = 0
        v = (n>>1)^n
        while v:
            if (v>>1&v) != v>>1:
                return False
            v >>= 1
        return True

