#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    祖玛游戏
"""

import copy


# 回溯方法 52ms
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        maxint = 1 << 32
        hm = dict()
        for h in hand:
            hm[h] = hm.get(h, 0) + 1

        boardlist = []
        d = 1
        last = None
        for x in board:
            if last == None:
                last = x
            elif last == x:
                d += 1
            else:
                boardlist.append((last, d))
                last = x
                d = 1
        boardlist.append((last, d))

        def dfs(bd, hm, p=0):
            if len(bd) == 0:
                return p
            minx = maxint
            for i, w in enumerate(bd):
                if w[0] in hm and hm[w[0]] + w[1] >= 3:

                    remain = bd[:i] + bd[i + 1:]
                    si = i - 1
                    sj = i + 1

                    while si >= 0 and sj < len(bd) and bd[si][0] == bd[sj][0] and bd[si][1] + bd[sj][1] >= 3:
                        si -= 1
                        sj += 1

                    if si >= 0 and sj < len(bd) and bd[si][0] == bd[sj][0]:
                        remain = bd[:si] + [(bd[si][0], bd[si][1] + bd[sj][1])] + bd[sj + 1:]
                    else:
                        remain = bd[:max(si + 1, 0)] + bd[sj:]
                    chm = copy.deepcopy(hm)
                    chm[w[0]] -= 3 - w[1]
                    res = dfs(remain, chm, p + 3 - w[1])

                    if res < minx:
                        minx = res
            return minx

        ans = dfs(boardlist, hm, 0)
        return -1 if ans == maxint else ans
