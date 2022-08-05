#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    IPO
"""
from typing import List

# 贪婪算法，自己构造链表 350ms
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        if len(Profits) < 1:
            return 0

        pc_list = [(p, Capital[i]) for i, p in enumerate(Profits)]
        pc_list.sort(key=lambda x: x[0], reverse=True)
        ds = DataStruct(pc_list[0][0], pc_list[0][1])
        root = ds
        for x, y in pc_list[1:]:
            ds.next = DataStruct(x, y)
            ds = ds.next
        nroot = DataStruct(0, 0)
        nroot.next = root
        nr = root
        for _ in range(k):
            pr = nroot
            nr = nroot.next
            while nr and nr.c > W:
                pr = nr
                nr = nr.next

            if nr is None:
                break
            else:
                W += nr.p
                nnr = nr.next
                nr.next = None
                pr.next = nnr

        return W


class DataStruct(object):

    def __init__(self, p, c):
        self.p = p
        self.c = c
        self.next = None

# 不同的数据结构，实现贪婪算法 292ms
class Solution2:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        if len(Profits) < 1:
            return 0

        pc_list = [x for x in zip(Profits, Capital)]
        pc_list.sort(key=lambda x: x[0])

        for _ in range(k):
            i = len(pc_list) - 1
            while i >= 0 and pc_list[i][1] > W:
                i -= 1

            if i < 0:
                break
            else:
                W += pc_list[i][0]
                pc_list.pop(i)

        return W


import heapq


# 将符合条件的capital对应的profits放入最大堆中，然后每次选择最大的
class Solution3:

    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:

        dp = [i for i in zip(Capital, Profits)]
        dp.sort()
        heap = []
        n, i = len(dp), 0
        while k:
            while i < n and dp[i][0] <= W:
                heapq.heappush(heap, -dp[i][1])
                i += 1
            if not heap:
                return W
            W += -heapq.heappop(heap)
            k -= 1
        return W
