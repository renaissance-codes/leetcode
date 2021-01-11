#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    出现次数最多的子树元素和
"""
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 后序遍历
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        result = defaultdict(int)

        def bfs(node):
            res = 0
            if node:
                left = bfs(node.left)
                right = bfs(node.right)

                res = node.val + left + right
                result[res] += 1

            return res

        bfs(root)

        if not result:
            return []

        nums = [(v, k) for k, v in result.items()]
        nums.sort(reverse=True)

        r = nums[0][0]
        return [x[1] for x in nums if x[0] == r]
