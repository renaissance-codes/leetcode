#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 动态规划的思路
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1:
            return [TreeNode(0)]
        plist = {
            0: [],
            1: [TreeNode(0)]
        }
        for i in range(2, N + 1):
            tresult = []
            for j in range(i - 1):

                left = j
                right = i - j - 1

                if len(plist[left]) and len(plist[right]):
                    for pl in plist[left]:
                        for pr in plist[right]:
                            ntree = TreeNode(0)
                            ntree.left = pl
                            ntree.right = pr
                            tresult.append(ntree)

            plist[i] = tresult
        return plist[N]