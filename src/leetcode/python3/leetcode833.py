#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    字符串的查找与替换
"""
from typing import List


# 先排序，然后逐条替换
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        if not indexes:
            return S
        indexex = [(x, i) for i, x in enumerate(indexes)]
        indexex.sort()
        start = 0
        result = []

        for inx, i in indexex:

            result.append(S[start:inx])
            ss = sources[i]
            st = S[inx:inx + len(ss)]
            if ss == st:
                result.append(targets[i])
            else:
                result.append(st)
            start = inx + len(ss)
        if start < len(S):
            result.append(S[start:])

        return "".join(result)
