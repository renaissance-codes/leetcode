#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    无重叠区间
"""
from typing import List


# 构建有向图
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: (x[1], x[1]))
        d_len = len(intervals)
        path = {}
        for i, x in enumerate(intervals):
            v = x[1]
            t = True
            for j in range(i + 1, d_len):
                if t:
                    if v <= intervals[j][0]:
                        path.setdefault(i, [])
                        path[i].append(j)
                        t = False
                        v = intervals[j][1]
                else:
                    if v <= intervals[j][0]:
                        break
                    else:
                        path[i].append(i)
                        v = min(intervals[j][1], v)

        max_res = 1
        max_d = {}
        for i in range(d_len - 1, -1, -1):
            if i not in path:
                max_d[i] = 1
            else:
                max_v = -1
                for p in path[i]:
                    if p not in max_d:
                        continue
                    max_v = max(max_d[p], max_v)
                max_res = max(max_v + 1, max_res)
                max_d[i] = max_v + 1
        return d_len - max_res


# 贪心算法
class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort()
        d_len = len(intervals)
        count = 1
        last = intervals[0]
        for x in intervals[1:]:
            if last[1] <= x[0]:
                count += 1
                last = x
            elif last[1] > x[1]:
                last = x

        return d_len - count
