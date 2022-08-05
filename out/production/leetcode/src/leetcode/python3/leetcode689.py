#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    三个无重叠数组的最大和
"""
from typing import List


# 动态规划思路
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        num_sum = [0]
        for n in nums:
            num_sum.append(n + num_sum[-1])
        d_len = len(nums)
        three = [(0, 0)] * d_len

        max_v = 0
        max_i = -1
        for i in range(d_len - 1, 2 * k - 1, -1):
            v = num_sum[i + 1] - num_sum[i + 1 - k]
            if v >= max_v:
                three[i] = (v, i - k + 1)
                max_i = i - k + 1
                max_v = v
            else:
                three[i] = (max_v, max_i)

        second = [(0, 0, 0)] * d_len
        max_v = 0
        max_ind = None
        for i in range(d_len - k - 1, k - 1, -1):
            v = num_sum[i + 1] - num_sum[i + 1 - k]
            vv, vi = three[i + k]
            if v + vv >= max_v:
                max_v = v + vv
                max_ind = (i - k + 1, vi)
                second[i] = (max_v, i - k + 1, vi)
            else:
                second[i] = (max_v, max_ind[0], max_ind[1])

        max_v = 0
        max_ind = None
        for i in range(d_len - 2 * k - 1, -1, -1):
            v = num_sum[i + 1] - num_sum[i + 1 - k]
            vv, vi, vii = second[i + k]
            if v + vv >= max_v:
                max_v = v + vv
                max_ind = [i - k + 1, vi, vii]

        return max_ind
