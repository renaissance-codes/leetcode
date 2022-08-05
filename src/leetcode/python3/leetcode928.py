#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

"""
    减少恶意软件的传播2
"""


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        d_len = len(graph)
        clean = set(range(d_len)) - set(initial)

        def dfs(index: int, seen):
            for i, v in enumerate(graph[index]):
                if v and i in clean and i not in seen:
                    seen.add(i)
                    dfs(i, seen)

        infected_by = {v: [] for v in clean}

        for v in initial:
            seen = set()
            dfs(v, seen)

            for u in seen:
                infected_by[u].append(v)

        contribute = {}
        for k, v in infected_by.items():
            if len(v) == 1:
                contribute.setdefault(v[0], 0)
                contribute[v[0]] += 1

        min_v = -1
        min_i = min(initial)
        for k, v in contribute.items():
            if v > min_v or (v == min_v and k < min_i):
                min_v = v
                min_i = k
        return min_i


# 广度优先做法，超时
class Solution2:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        d_len = len(graph)

        def findMin(index: int) -> int:
            n_set = set(initial)
            n_queue = []
            for x in initial:
                if x != index:
                    n_queue.append(x)

            while len(n_queue):
                q = n_queue.pop()
                for i in range(d_len):
                    if graph[i][q] and i not in n_set:
                        n_queue.append(i)
                        n_set.add(i)
            return len(n_set)

        min_v = float("inf")
        min_i = -1
        for i in initial:
            mv = findMin(i)
            if mv < min_v or (mv == min_v and i < min_i):
                min_v = mv
                min_i = i

        return min_i
