#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    两个字符串的最小ASCII删除和
"""


# dp algorithm
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1d = len(s1)
        s2d = len(s2)

        d = [[0 for i in range(s2d + 1)] for j in range(s1d + 1)]

        for i in range(s1d):
            for j in range(s2d):
                if s1[i] == s2[j]:
                    d[i + 1][j + 1] = max([d[i][j + 1], d[i + 1][j], d[i][j] + ord(s1[i])])
                else:
                    d[i + 1][j + 1] = max([d[i][j + 1], d[i + 1][j]])

        s1ascii = sum([ord(x) for x in s1])
        s2ascii = sum([ord(x) for x in s2])

        return s1ascii + s2ascii - 2 * d[s1d][s2d]
