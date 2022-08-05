#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    矩形面积 II
"""
from typing import List


# 扫描的原理 + 离散化
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        xset = set()

        for x1, y1, x2, y2 in rectangles:
            xset.add(x1)
            xset.add(x2)
        xlist = sorted(list(xset))

        d = {}
        dc = {}
        for i in range(len(xlist) - 1):
            d[xlist[i]] = xlist[i + 1]
            dc[xlist[i]] = {}

        for x1, y1, x2, y2 in rectangles:

            sx = x1
            while sx < x2:
                dc[sx].setdefault(y1, 0)
                dc[sx][y1] = max(dc[sx][y1], y2)
                sx = d[sx]

        ans = 0
        for k, v in dc.items():
            cur = 0
            for vi in sorted(v):
                if cur < v[vi]:
                    if vi < cur:
                        ans += (v[vi] - cur) * (d[k] - k)
                    else:
                        ans += (v[vi] - vi) * (d[k] - k)
                    cur = v[vi]
        return ans % mod
