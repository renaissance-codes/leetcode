#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    斐波那契数
"""

class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N

        first = 0
        second = 1

        for _ in range(2, N + 1):
            first, second = second, first + second

        return second
