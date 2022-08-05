#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    数组中的最长山脉
"""
from typing import List


# 使用状态变量
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        start = None
        sv = None
        maxlen = 0
        flag = 0
        for i, x in enumerate(A):
            if i > 0:
                if x > sv:
                    if flag == -1:
                        leng = i-start
                        maxlen = max(leng, maxlen)
                    if flag != 1:
                        start = i-1
                        flag = 1
                elif x < sv:
                    if (flag == 1 or flag == -1):
                        flag = -1
                    else:
                        flag = 0
                else:
                    if flag == -1:
                        leng = i-start
                        maxlen = max(leng, maxlen)
                    flag = 0
            sv = x
        if flag == -1:
            maxlen = max(maxlen, len(A)-start)
        return maxlen
