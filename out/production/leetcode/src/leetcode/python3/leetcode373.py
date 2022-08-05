#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    查找和最小的K对数字
"""
import heapq
from typing import List


# 使用循环对比
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if k == 0:
            return res
        d1 = len(nums1)
        d2 = len(nums2)
        if d1 == 0 or d2 == 0:
            return res
        qs = [[i, 0] for i in range(d1)]
        s = 0

        while s < k:
            mini, minj = -1, -1
            minv = 1 << 32
            for x, y in qs:
                if y >= d2:
                    continue
                if nums1[x] + nums2[y] < minv:
                    minv = nums1[x] + nums2[y]
                    mini, minj = x, y
            if mini == -1:
                break
            res.append([nums1[mini], nums2[minj]])
            qs[mini][1] += 1
            s += 1
        return res


# 使用堆来进行动态选取最小值
class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if k == 0:
            return res
        d1 = len(nums1)
        d2 = len(nums2)
        if d1 == 0 or d2 == 0:
            return res
        qs = [[nums1[i] + nums2[0], i, 0] for i in range(d1)]
        heapq.heapify(qs)
        s = 0

        while s < k:
            if len(qs):
                x, i, j = heapq.heappop(qs)
                res.append([nums1[i], nums2[j]])
                if j < d2 - 1:
                    heapq.heappush(qs, [nums1[i] + nums2[j + 1], i, j + 1])
            else:
                break
            s += 1
        return res

