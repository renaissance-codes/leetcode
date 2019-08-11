#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    求解二叉树的直径
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 暴力求解， 将左子树和右子树以及两个子树的深度进行比较, 576ms
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        max_len = 0
        both_deep = 0
        if root.left:
            left_len = self.diameterOfBinaryTree(root.left)
            if left_len > max_len:
                max_len = left_len
            both_deep += self.getDeep(root.left)

        if root.right:
            right_len = self.diameterOfBinaryTree(root.right)
            if right_len > max_len:
                max_len = right_len
            both_deep += self.getDeep(root.right)
        if both_deep > max_len:
            max_len = both_deep

        return max_len

    def getDeep(self, root: TreeNode) -> int:
        d = [root]
        deep = 0
        while len(d):
            new_d = []
            for x in d:
                if x.left:
                    new_d.append(x.left)
                if x.right:
                    new_d.append(x.right)
            deep += 1

            d = new_d
        return deep


# 60ms 使用类变量存储最大直径
class Solution2:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        self.max_len = 0

        self.maxDeep(root)

        return self.max_len

    def maxDeep(self, node):
        if node is None:
            return 0
        left = self.maxDeep(node.left)
        right = self.maxDeep(node.right)

        if left + right > self.max_len:
            self.max_len = left + right

        return max(left, right) + 1