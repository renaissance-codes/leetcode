#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    递增顺序查找树
"""


class TreeNode:

    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tn = TreeNode(-1)

        def dfs(nd, tn):
            if nd:
                if nd.left:
                    tn = dfs(nd.left, tn)
                tn.right = TreeNode(nd.val)
                tn = tn.right
                if nd.right:
                    tn = dfs(nd.right, tn)
            return tn

        nn = dfs(root, tn)
        return tn.right


# stack 方法
class Solution2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tn = TreeNode(-1)
        nt = tn

        stack = [root]
        while stack:
            p = stack.pop()
            if type(p) == int:
                nt.right = TreeNode(p)
                nt = nt.right
            else:
                if p.right:
                    stack.append(p.right)
                stack.append(p.val)
                if p.left:
                    stack.append(p.left)

        return tn.right


# 二叉树的内部变换
class Solution3:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tn = TreeNode(-1)
        self.cur = tn

        def morder(node):
            if node:
                morder(node.left)
                self.cur.right = node
                node.left = None
                self.cur = node
                morder(node.right)

        morder(root)

        return tn.right
