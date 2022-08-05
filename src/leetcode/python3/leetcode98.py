#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    验证二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归运行，返回该树的最大最小值， 64ms
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_node(node):
            if node is None:
                return True, None, None
            left_min = None
            if node.left:
                lt, left_max, left_min = check_node(node.left)
                if not lt or left_max >= node.val:
                    return False, None, None
            right_max = None
            if node.right:
                rt, right_max, right_min = check_node(node.right)
                if not rt or right_min <= node.val:
                    return False, None, None

            if not node.left and not node.right:
                return True, node.val, node.val

            if left_min is None:
                left_min = node.val
            if right_max is None:
                right_max = node.val

            return True, right_max, left_min

        state, lf, tg = check_node(root)
        return state


# 中序遍历，68ms, 使用yeild
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def check_node(node):
            if node.left:
                for nd in check_node(node.left):
                    yield nd
            yield node.val

            if node.right:
                for nd in check_node(node.right):
                    yield nd

        s = float("-inf")
        for x in check_node(root):
            if x <= s:
                return False
            s = x
        return True