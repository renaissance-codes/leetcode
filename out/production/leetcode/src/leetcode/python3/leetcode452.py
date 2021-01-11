#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    用最少数量的箭引爆气球
"""
from typing import List


# 先排序，在计算重复部分 740ms
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        order_points = sorted(points, key=lambda x: x[0])
        num = 0
        cal = order_points[0]
        for x in order_points[1:]:
            overlap = self.findOverLap(cal, x)
            if not overlap:
                num += 1
                cal = x
            else:
                cal = overlap
        if cal:
            num += 1
        return num

    def findOverLap(self, pointsA: List[int], pointsB: List[int]) -> List[int]:

        if pointsA[1] < pointsB[0]:
            return []
        else:
            return [pointsB[0], min(pointsA[1], pointsB[1])]


# 思路一样，进行稍微改进，600ms
class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        points.sort(key=lambda x: x[1])
        num = 1
        end = points[0][1]
        for x in points[1:]:
            if x[0] > end:
                num += 1
                end = x[1]

        return num
