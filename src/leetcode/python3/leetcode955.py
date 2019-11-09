#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    删列造序 II
"""
from typing import List


# 想岔了，找到第一列符合条件就好办了
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        a_len = len(A)
        cur = [""] * a_len

        def is_sort(alist):
            last = ""
            for e in alist:
                if last > e:
                    return False
                last = e
            return True

        ans = 0
        for cor in zip(*A):

            cur2 = cur[:]
            for i, x in enumerate(cor):
                cur2[i] += x

            if is_sort(cur2):
                cur = cur2
            else:
                ans += 1

        return ans


# 贪心算法
class Solution2:
    def minDeletionSize(self, A: List[str]) -> int:
        a_len = len(A)
        cut = [0] * a_len

        ans = 0
        for cor in zip(*A):
            if all([cut[i] or cor[i] <= cor[i + 1] for i in range(a_len - 1)]):
                for i in range(a_len - 1):
                    if cor[i] < cor[i + 1]:
                        cut[i] = True
            else:
                ans += 1

        return ans
