#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    交错字符串
"""


# 使用带记忆的回溯
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        s1d = len(s1)
        s2d = len(s2)
        s3d = len(s3)

        if s1d + s2d != s3d:
            return False
        cache = {}

        def is_interleave(sa, sb, sc):
            if len(sa) == 0:
                if sb != sc:
                    return False
                else:
                    return True
            elif len(sb) == 0:
                if sa != sc:
                    return False
                else:
                    return True

            if sa[0] == sb[0]:
                if sa[0] == sc[0]:
                    firstk = (sa[1:], sb, sc[1:])
                    if firstk in cache:
                        first = cache[firstk]
                    else:
                        first = is_interleave(sa[1:], sb, sc[1:])
                        cache[firstk] = first
                    if first:
                        return True
                    secondk = (sa, sb[1:], sc[1:])
                    if secondk in cache:
                        second = cache[secondk]
                    else:
                        second = is_interleave(sa, sb[1:], sc[1:])
                        cache[firstk] = second
                    return second
                else:
                    return False

            else:
                if sa[0] == sc[0]:
                    rs = is_interleave(sa[1:], sb, sc[1:])
                    return rs
                elif sb[0] == sc[0]:
                    return is_interleave(sa, sb[1:], sc[1:])
                else:
                    return False

        return is_interleave(s1, s2, s3)


# 动态规划
class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        s1d = len(s1)
        s2d = len(s2)
        s3d = len(s3)
        if s1d + s2d != s3d:
            return False

        dc = [[-1 for i in range(s2d + 1)] for j in range(s1d + 1)]
        dc[0][0] = 1
        for i in range(s1d):
            ans = 1 if s1[i] == s3[i] else 0

            dc[i + 1][0] = 1 if dc[i][0] and ans else 0

        for i in range(s2d):
            dc[0][i + 1] = 1 if dc[0][i] and s2[i] == s3[i] else 0

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                dc[i + 1][j + 1] = 0
                if (s3[i + j + 1] == s1[i] and dc[i][j + 1]) or (s3[i + j + 1] == s2[j] and dc[i + 1][j]):
                    dc[i + 1][j + 1] = 1

        return dc[s1d][s2d]
