#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    二叉树的前序遍历
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


# 递归方法
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return result
