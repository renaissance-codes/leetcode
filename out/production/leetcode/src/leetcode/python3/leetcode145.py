#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    二叉树的后序遍历
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 使用stack 52ms
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while len(stack):
            p = stack.pop()
            if isinstance(p, int):
                result.append(p)
            else:
                stack.append(p.val)
                if p.right:
                    stack.append(p.right)
                if p.left:
                    stack.append(p.left)
        return result

# 递归思路 36ms
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result