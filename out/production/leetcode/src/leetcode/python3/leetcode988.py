#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    从叶节点开始的最小字符串
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 将所有字符串列出，然后比较 72ms
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:

        result = []

        def dfs(node, s):
            if node.left is None and node.right is None:
                result.append(chr(node.val + 97) + s)
            if node.left:
                dfs(node.left, chr(node.val + 97) + s)
            if node.right:
                dfs(node.right, chr(node.val + 97) + s)

        dfs(root, "")
        return min(result)

