#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    最近的K个元素
"""
from typing import List


# 先得到绝对差值，然后进行排序
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n_arr = []
        min_i = -1
        min_v = float("inf")

        for i, xv in enumerate(arr):
            abs_v = abs(xv - x)
            if min_v > abs_v:
                min_v = abs_v
                min_i = i
            n_arr.append(abs_v)

        if min_i == 0:
            return arr[:k]
        result_arr = [arr[min_i]]
        ki = 1
        left_i = min_i
        right_i = min_i

        while ki < k:
            if left_i - 1 < 0:
                result_arr.append(arr[right_i + 1])
                right_i += 1
            elif right_i + 1 >= len(arr):
                result_arr.append(arr[left_i - 1])
                left_i -= 1
            else:
                if n_arr[left_i - 1] <= n_arr[right_i + 1]:
                    result_arr.append(arr[left_i - 1])
                    left_i -= 1
                else:
                    result_arr.append(arr[right_i + 1])
                    right_i += 1
            ki += 1

        result_arr.sort()
        return result_arr
