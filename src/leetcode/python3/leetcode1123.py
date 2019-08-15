#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    最深叶节点的最近祖先
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用队列
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        def maxDeep(node, dp):
            if node:
                dp = max(maxDeep(node.left, dp + 1), maxDeep(node.right, dp + 1))
            return dp

        queue = [root]
        while len(queue):
            q = queue.pop(0)
            lf_dp = maxDeep(q.left, 0)
            rg_dp = maxDeep(q.right, 0)
            if lf_dp > rg_dp:
                queue.append(q.left)
            elif lf_dp < rg_dp:
                queue.append(q.right)
            else:
                return q

        return root

# 递归方法
class Solution2:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        def maxDeep(node):
            if node is None:
                return node, 0

            lf_nd, lf_dp = maxDeep(node.left)
            rg_nd, rg_dp = maxDeep(node.right)

            if lf_dp == rg_dp:
                return node, lf_dp + 1
            elif lf_dp > rg_dp:
                return lf_nd, lf_dp + 1
            else:
                return rg_nd, rg_dp + 1

        nd, _ = maxDeep(root)

        return nd