#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    权重随机数
"""
import random
from typing import List
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sum_w = sum(w)
        x = 0
        self.cal = []
        for wx in w:
            x += wx
            self.cal.append(x)

    def pickIndex(self) -> int:
        rd = random.random()*self.sum_w//1
        left_ind = 0
        right_ind = len(self.cal)-1
        while left_ind < right_ind:
            mid = (left_ind+right_ind)//2
            if self.cal[mid] == rd:
                return mid+1
            elif self.cal[mid] > rd:
                right_ind = mid
            else:
                left_ind = mid+1
        return left_ind