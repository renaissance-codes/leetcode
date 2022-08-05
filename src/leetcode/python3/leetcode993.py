#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    判断树的堂兄弟节点，即两个节点属于同一层，但是没有同一个父亲
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 使用广度优先的方法，一层层遍历 40ms,
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        queue = [root]
        while queue:
            nqueue = []
            x_match = False
            x_p = None
            y_match = False
            y_p = None
            for q in queue:
                if q.left:
                    if not x_match and q.left.val == x:
                        x_match = True
                        x_p = q.val
                    if not y_match and q.left.val == y:
                        y_match = True
                        y_p = q.val
                    nqueue.append(q.left)
                if q.right:
                    if not x_match and q.right.val == x:
                        x_match = True
                        x_p = q.val
                    if not y_match and q.right.val == y:
                        y_match = True
                        y_p = q.val
                    nqueue.append(q.right)

                if x_match and y_match:
                    if x_p == y_p:
                        return False
                    else:
                        return True
            if x_match or y_match:
                return False

            queue = nqueue
        return False

# 寻找对应节点的层数以及父节点，然后比较
