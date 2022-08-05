#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 二叉树的深度
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归， 深度优先 56ms
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            left_d = dfs(node.left)
            right_d = dfs(node.right)

            return max(left_d, right_d) + 1

        return dfs(root)