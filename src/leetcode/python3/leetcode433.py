#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    最小基因变化
"""
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [start]

        def score(xt, yt):
            sc = 0
            for i, x in enumerate(xt):
                if yt[i] != x:
                    sc += 1
                if sc > 1:
                    return False
            return sc == 1

        step = 0
        while bank:
            resq = []
            res = bank
            for q in queue:
                tres = []
                for x in res:
                    if score(q, x):
                        if x == end:
                            return step + 1
                        resq.append(x)
                    else:
                        tres.append(x)
                res = tres
            if len(res) == len(bank):
                return -1
            queue = resq
            bank = res

            step += 1

        return -1


# 广度优先
class Solution2:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = [start]
        step = 0
        mp = {"A": "CGT", "C": "AGT", "G": "ACT", "T": "ACG"}
        while queue:
            nq = []
            for q in queue:
                for i in range(8):
                    for x in mp[q[i]]:
                        muta = q[:i] + x + q[i + 1:]
                        if muta in bank_set:
                            if muta == end:
                                return step + 1
                            nq.append(muta)
                            bank_set.remove(muta)
            queue = nq
            step += 1

        return -1
