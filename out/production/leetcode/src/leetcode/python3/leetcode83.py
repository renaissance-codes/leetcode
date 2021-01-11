#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    删除排序链表中的重复元素
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 需要存储上一个链表节点 60ms
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nhead = head
        lhead = head
        n_val = None
        while nhead:
            if nhead.val == n_val:
                nhead = nhead.next
                lhead.next = nhead
            else:
                n_val = nhead.val
                lhead = nhead
                nhead = nhead.next
        return head


# 不存上一个节点 52ms
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nhead = head
        while nhead and nhead.next:
            if nhead.val == nhead.next.val:
                nhead.next = nhead.next.next
            else:
                nhead = nhead.next
        return head
