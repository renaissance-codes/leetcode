#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    二叉树的所有路径
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用递归方法
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if root is None:
            return result
        def dfs(node, path):
            if node.left:
                dfs(node.left, path+"{}->".format(node.val))
            if node.right:
                dfs(node.right, path+"{}->".format(node.val))
            if not node.left and not node.right:
                result.append(path+"{}".format(node.val))
        dfs(root, "")
        return result