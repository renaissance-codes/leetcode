#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    两数相加
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 使用栈来解决
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        stack1 = []

        n2 = l2
        stack2 = []

        while n1:
            stack1.append(n1)
            n1 = n1.next

        while n2:
            stack2.append(n2)
            n2 = n2.next
        nd = None
        ind = 0
        while stack1 and stack2:
            s1 = stack1.pop()
            s2 = stack2.pop()

            val = s1.val + s2.val + ind
            nnd = val % 10
            ind = val // 10

            s1.val = nnd
            s1.next = nd
            nd = s1

        def get_node(stack, snod, ind, nd):
            while ind and stack:
                s1 = stack.pop()
                val = s1.val + ind
                nnd = val % 10
                ind = val // 10

                s1.val = nnd
                s1.next = nd
                nd = s1
            if stack:
                s = stack[-1]
                s.next = nd
                return snod
            elif ind:
                nod = ListNode(ind)
                nod.next = nd
                return nod
            else:
                return nd

        if stack1:
            return get_node(stack1, l1, ind, nd)
        elif stack2:
            return get_node(stack2, l2, ind, nd)
        else:
            if ind:
                nod = ListNode(ind)
                nod.next = nd
                return nod
            else:
                return nd


# 使用递归来做， 84ms
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_len(node):
            n = node
            n_len = 0
            while n:
                n_len += 1
                n = n.next
            return n_len

        n1len = get_len(l1)
        n2len = get_len(l2)

        if n2len > n1len:
            l1, l2 = l2, l1
            n1len, n2len = n2len, n1len

        n1 = l1
        n_len = n1len - n2len

        nh = ListNode(0)
        while n_len:
            nh = n1
            n1 = n1.next
            n_len -= 1

        def dp(nd1, nd2):
            if nd1 is None:
                return 0
            ind = dp(nd1.next, nd2.next)
            val = ind + nd1.val + nd2.val
            nnd = val % 10
            ind = val // 10
            nd1.val = nnd

            return ind

        def dp2(nd, leng, indv):
            if leng < 1:
                return indv
            elif leng == 1:
                val = indv + nd.val
                nnd = val % 10
                ind = val // 10
                nd.val = nnd

                return ind
            else:
                if indv:
                    indv = dp2(nd.next, leng - 1, indv)
                    val = indv + nd.val
                    nnd = val % 10
                    indv = val // 10
                    nd.val = nnd

                return indv

        indv = dp(n1, l2)

        indv = dp2(l1, n1len - n2len, indv)
        if indv:
            node = ListNode(indv)
            node.next = l1
            return node
        else:
            return l1


# 反转链表
class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverse(node):
            last = None
            while node:
                nnd = node
                node = node.next
                nnd.next = last
                last = nnd
            return last

        l1reverse = reverse(l1)
        l2reverse = reverse(l2)

        node = None
        ind = 0
        while l1reverse or l2reverse or ind:
            lva1 = 0
            if l1reverse:
                lva1 = l1reverse.val
                l1reverse = l1reverse.next

            lva2 = 0
            if l2reverse:
                lva2 = l2reverse.val
                l2reverse = l2reverse.next

            val = lva1 + lva2 + ind
            nnd = val % 10
            ind = val // 10

            nd = ListNode(nnd)
            nd.next = node
            node = nd
        return node
