#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    颜色交替的最短路径
"""
from typing import List


# 广度优先
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_dic = {}
        blue_dic = {}
        for x, y in red_edges:
            red_dic.setdefault(x, [])
            red_dic[x].append(y)
        for x, y in blue_edges:
            blue_dic.setdefault(x, [])
            blue_dic[x].append(y)

        res = [-1] * n
        res[0] = 0
        rset = {0}
        bset = {0}

        step = 1
        red_start = [0]
        blue_start = [0]
        while True:
            nred = []
            for x in red_start:
                for y in red_dic.get(x, []):
                    if y in rset:
                        continue
                    rset.add(y)
                    nred.append(y)
                    if res[y] == -1:
                        res[y] = step

            nblue = []
            for x in blue_start:
                for y in blue_dic.get(x, []):
                    if y in bset:
                        continue
                    bset.add(y)
                    nblue.append(y)
                    if res[y] == -1:
                        res[y] = step
            if len(nblue) == 0 and len(nred) == 0:
                break
            blue_start = nred
            red_start = nblue
            step += 1
        return res
