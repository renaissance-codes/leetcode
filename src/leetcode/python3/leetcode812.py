#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 动态规划
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        d = {}
        num = 0
        mod = 10 ** 9 + 7

        for s in S:
            if s not in d:
                d[s] = num
                num += num + 1

            else:
                x = d[s]
                d[s] = num
                num += num - x

        return num % mod
