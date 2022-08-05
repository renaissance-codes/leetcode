#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    扁平化多级双向链表
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# 使用栈的方法 1348ms
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        nhead = Node(0, None, None, None)
        cur_node = nhead
        stack = [head]
        while len(stack):
            q = stack.pop()
            cur_node.next = q
            q.prev = cur_node

            if q.next:
                stack.append(q.next)
            if q.child:
                stack.append(q.child)
                q.child = None

            cur_node = q
        thead = nhead.next
        thead.prev = None

        return thead


# 使用递归方法 1320
class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        nhead = Node(0, None, None, None)
        cur_node = nhead

        def dfs(node, c_node):
            c_node.next = node
            node.prev = c_node
            node_next = node.next
            cl_node = node.child
            node.child = None

            if cl_node:
                node = dfs(cl_node, node)

            if node_next:
                node = dfs(node_next, node)

            return node

        dfs(head, cur_node)
        thead = nhead.next
        thead.prev = None

        return thead

# 比较简洁的方法 2088ms
from itertools import chain

class Solution3:
    def flatten(self, head: 'Node') -> 'Node':
        def gen(n): yield from chain([n], gen(n.child), gen(n.next)) if n else ()
        iters = gen(head); p = head and next(iters)
        for n in iters: p.next, n.prev, p.child, n.child, p = n, p, None, None, n
        return head
