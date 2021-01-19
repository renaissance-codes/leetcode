#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    判断给定的数字集合是否可以组成一个2的幂指数
"""

import math


# 暴力求解，将位数相同的幂指数和目标数字进行匹配，查看数字的字典是否相同， 52ms
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N == 1:
            return True
        num_map, figure = self.getNumMap(N)

        figure_dict = {}
        start_num = 1
        for i in range(1, 30):

            start_num *= 2
            potential_figure = math.log(start_num) / math.log(10) // 1 + 1

            if figure == potential_figure:
                potential_map, _ = self.getNumMap(start_num)

                match_num = 0
                for k, v in potential_map.items():
                    if k in num_map and num_map[k] == v:
                        match_num += 1
                    else:
                        break
                if match_num == len(potential_map):
                    return True
            elif figure < potential_figure:
                break

        return False

    def getNumMap(self, num: int):

        num_map = dict()
        figure = 0
        while num:
            ts = num % 10
            num_map.setdefault(ts, 0)
            num_map[ts] += 1
            num //= 10
            figure += 1
        return num_map, figure