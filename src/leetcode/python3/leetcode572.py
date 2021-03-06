#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

    另一颗树的子树
"""

class TreeNode:

    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return True
        if s is None:
            return False

        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)