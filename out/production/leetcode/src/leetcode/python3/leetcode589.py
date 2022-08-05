#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    N叉树的前序遍历
"""
from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# 迭代法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            q = queue.pop()
            res.append(q.val)

            for k in q.children[::-1]:
                queue.append(k)
        return res


# 递归解法
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []

        def dfs(node):
            res.append(node.val)

            for nd in node.children:
                dfs(nd)
        dfs(root)
        return res
