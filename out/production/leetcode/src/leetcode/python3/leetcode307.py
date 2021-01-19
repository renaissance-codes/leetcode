#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    区域和检索--数组可修改
"""
from typing import List


# 使用dict存储变化值
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cal = [0]
        for n in nums:
            self.cal.append(self.cal[-1]+n)
        self.upd = {}

    def update(self, i: int, val: int) -> None:
        self.upd[i] = val

    def sumRange(self, i: int, j: int) -> int:
        val = self.cal[j+1] - self.cal[i]
        for k, v in self.upd.items():
            if i<=k<=j:
                val += v-self.nums[k]
        return val


# 线段树实现
class NumArray2:

    def __init__(self, nums: List[int]):
        d_len = len(nums)
        self.tree = [0] * 2 * d_len

        for i, x in enumerate(nums):
            self.tree[i + d_len] = x

        for i in range(d_len - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
        self.d_len = d_len

    def update(self, i: int, val: int) -> None:
        t = i + self.d_len
        oval = self.tree[t]
        while t:
            self.tree[t] += val - oval
            t >>= 1

    def sumRange(self, i: int, j: int) -> int:
        i += self.d_len
        j += self.d_len

        sumv = 0
        while i <= j:
            if i % 2 == 1:
                sumv += self.tree[i]
                i += 1

            if j % 2 == 0:
                sumv += self.tree[j]
                j -= 1
            i >>= 1
            j >>= 1
        return sumv


import math

# sqrt 分解
class NumArray2:

    def __init__(self, nums: List[int]):
        d_len = len(nums)
        if d_len == 0:
            self.nums = nums
            self.bin = [0] * d_len
            self.blen = 0
        else:
            sqrt_len = math.sqrt(d_len)
            self.blen = math.ceil(d_len / sqrt_len)
            self.nums = nums
            self.bin = [0] * self.blen

            for i in range(self.blen):
                self.bin[i] = sum(nums[i * self.blen:(i + 1) * self.blen])

    def update(self, i: int, val: int) -> None:
        oval = self.nums[i]
        t = int(i // self.blen)
        self.bin[t] += val - oval
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        start_bin = int(i // self.blen)
        end_bin = int(j // self.blen)
        sumv = 0
        if start_bin == end_bin:
            for k in range(i, j + 1):
                sumv += self.nums[k]
        elif start_bin < end_bin:
            for k in range(i, (start_bin + 1) * self.blen):
                sumv += self.nums[k]

            for k in range(start_bin + 1, end_bin):
                sumv += self.bin[k]

            for k in range(end_bin * self.blen, j + 1):
                sumv += self.nums[k]

        return sumv
