#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    4的幂
"""
import math


# 循环求解 52ms
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        rest = num % 4
        while rest == 0 and num > 1:
            num >>= 2
            rest = num % 4

        return num == 1


# 位移求解 48ms
class Solution2:
    def isPowerOfFour(self, num: int) -> bool:
        t = 1
        while t <= num:

            if t & num == num:
                return True

            t <<= 2
        return False


# 使用log 函数
class Solution3:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return math.log(num)/math.log(4)%1 == 0

# 先判断是否是幂指数，然后判断是否是4的幂指数
class Solution4:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0 or num & num - 1:
            return False

        return 0x55555555 & num
