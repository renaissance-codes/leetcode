#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 使用减法原则
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_x = len(nums)
        for i, x in enumerate(nums):
            sum_x += i-x
        return sum_x
