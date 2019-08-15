#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    二叉树的层次遍历II
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 使用队列方法
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = [root]

        while len(queue):
            level_result = []
            n_queue = []
            for q in queue:
                level_result.append(q.val)
                if q.left:
                    n_queue.append(q.left)
                if q.right:
                    n_queue.append(q.right)
            result.append(level_result)
            queue = n_queue
        return result[::-1]
