#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    移动石子直到连续
"""
from typing import List


# 分开进行求解，196ms
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()

        distance = []
        last_one = None
        num = 0
        result = []
        max_len = -1
        for x in stones:
            if last_one:
                distance.append(x - last_one - 1)
                if x - last_one > 1:
                    num += 1
            result.append(x)
            while result[-1] - result[0] > len(stones) - 1:
                result.pop(0)
            max_len = max(len(result), max_len)
            last_one = x
        sum_dis = sum(distance)
        if not sum_dis:
            return [0, 0]
        max_v = sum_dis - min(distance[-1], distance[0])

        blank_len = len(stones) - max_len
        if num == 1 and (distance[-1] > 0 or distance[0] > 0):
            min_v = min(blank_len + 1, sum_dis)
        else:
            min_v = blank_len
        return [min_v, max_v]

# 优化到180ms
class Solution2:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        d_len = len(stones)
        if stones[-1] - stones[0] == d_len - 1:
            return [0, 0]
        dlon = stones[-1] - stones[0] - d_len + 1
        max_v = dlon - min(stones[-1] - stones[-2] - 1, stones[1] - stones[0] - 1)
        min_v = max_v

        j = 0
        for i in range(d_len):
            while stones[i] - stones[j] + 1 > d_len:
                j += 1

            cost = d_len - i + j - 1
            min_v = min(cost, min_v)
        if (stones[-1] - stones[-2] - 1) == dlon or (stones[1] - stones[0] - 1) == dlon:
            min_v = min(dlon, 2)
        return [min_v, max_v]







