#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    N叉树的后序遍历
"""
from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

# 使用stack, 做到真正后续遍历 1104ms
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        path_set = set()
        result = []
        if root is None:
            return result
        stack = [root]

        while len(stack):
            q = stack.pop()
            if q in path_set:
                result.append(q.val)
            else:
                path_set.add(q)
                q_child = q.children
                stack.append(q)

                for xq in q_child[::-1]:
                    if xq:
                        stack.append(xq)
        return result


# 使用stack 将数值进行前插 992ms
class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]

        while len(stack):
            q = stack.pop()
            result.insert(0, q.val)
            for xq in q.children:
                stack.append(xq)
        return result