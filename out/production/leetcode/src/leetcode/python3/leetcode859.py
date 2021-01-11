#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    亲密字符串
"""


# 可交换的分为两种情况：（1）A B字符串完全相同，同时字符串中存在重复字符
#                      （2）A B字符串有两处不同，两处不同的地方调换一下是相同的
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) == 0 or len(B) == 0:
            return False
        a_set = set()
        has_repeat = False
        dif_num = 0
        dif_index = []
        for i, x in enumerate(A):
            if x in a_set:
                has_repeat = True
            else:
                a_set.add(x)
            if x != B[i]:
                dif_num += 1
                dif_index.append(i)
            if dif_num > 2:
                return False

        if dif_num == 0:
            return has_repeat
        elif dif_num == 2:
            return A[dif_index[0]] == B[dif_index[1]] and A[dif_index[1]] == B[dif_index[0]]

        return False