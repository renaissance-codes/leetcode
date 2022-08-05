#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    使数组唯一的最小增量
"""


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        ans = 0

        aset = dict()
        for x in A:
            aset.setdefault(x, 0)
            aset[x] += 1

        alist = [(k, v - 1) for k, v in aset.items() if v > 1]
        if len(alist) == 0:
            return 0
        alist.sort(key=lambda x: x[0])

        dl = sum([k * v for k, v in alist])

        dm = 0
        k = None
        v = None
        start = -2
        while len(alist) or v:
            if k is None:
                k, v = alist.pop(0)
                start = max(k + 1, start + 1)

            while start in aset:
                start += 1
            aset[start] = 1
            dm += start
            v -= 1

            if v == 0:
                k = None

        return dm - dl