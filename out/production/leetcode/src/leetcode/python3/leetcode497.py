#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    非重叠矩阵中的随机点
"""

import random
from typing import List


# 按照面积分配每个矩阵的选择概率，然后随机选取矩阵上的点
# 224ms
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        self.weight = [0]
        for rec in self.rects:
            rec_area = (rec[2] + 1 - rec[0]) * (rec[3] + 1 - rec[1])
            self.weight.append(rec_area + self.weight[-1])
        self.all_area = self.weight[-1]

    def pick(self) -> List[int]:
        rect_value = random.random() * self.all_area
        rect_index = self.get_index(rect_value)
        rect = self.rects[rect_index]

        x = int(random.random() * (rect[2] - rect[0] + 1)) + rect[0]
        y = int(random.random() * (rect[3] - rect[1] + 1)) + rect[1]
        return [x, y]

    def get_index(self, value):
        for i, x in enumerate(self.weight):
            if value < x:
                return i - 1
        return