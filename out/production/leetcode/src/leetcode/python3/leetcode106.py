#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    从中序与后序遍历序列构造二叉树
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        rval = postorder[-1]

        rind = inorder.index(rval)

        leftv = inorder[:rind]
        rightv = inorder[rind + 1:]

        pleftv = postorder[:rind]
        prightv = postorder[rind:-1]

        root = TreeNode(rval)
        root.left = self.buildTree(leftv, pleftv)
        root.right = self.buildTree(rightv, prightv)

        return root
