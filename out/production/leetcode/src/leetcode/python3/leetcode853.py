#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    车队问题
"""
from typing import List

"""
    先计算到达目的地的时间，然后按照位置从大到小进行排序
    如果后面的时间小于前面位置的时间，那么就可以合并，并且和后面的时间相同，
    272ms
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 2:
            return len(position)
        nposition = [(p, (target - p) / speed[i]) for i, p in enumerate(position)]
        nposition.sort(reverse=True)

        num = len(position)
        sp, ss = nposition[0]
        for _, si in nposition[1:]:
            if ss >= si:
                num -= 1
            else:
                ss = si
        return num