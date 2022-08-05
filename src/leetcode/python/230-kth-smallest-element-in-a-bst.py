#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author  :   https://github.com/xixici
Date    :   2019/8/23
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        listA = []
        listB = self.midOrder(listA, root)
        return listB[k - 1]

    def midOrder(self, listA, root):
        if not root:
            return listA
        self.midOrder(listA, root.left)
        listA.append(root.val)
        self.midOrder(listA, root.right)
        return listA
