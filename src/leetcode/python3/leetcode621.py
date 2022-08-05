#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    任务调度器
"""
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dlen = len(tasks)
        d = {}
        for task in tasks:
            d.setdefault(task, 0)
            d[task] += 1

        heap = [v for k, v in d.items()]
        heap.sort(reverse=True)

        length = heap[0]

        nv = sum([1 if x == length else 0 for x in heap[:n]])
        res = (length - 1) * (n + 1) + nv

        return res if res > dlen else dlen
