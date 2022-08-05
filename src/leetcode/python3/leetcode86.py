#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    分割链表
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 寻找首个大于等于目标值的节点，然后不断将小于的节点进行插入操作 44ms
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return head
        phead = ListNode(0)
        phead.next = head
        first_last = None
        first_node = None
        cur = head
        cur_last = phead

        while cur:
            if cur.val < x:
                if first_node:
                    cur_next = None
                    if cur.next:
                        cur_next = cur.next
                        cur.next = None
                    cur_last.next = cur_next

                    cur.next = first_node
                    if first_last:
                        first_last.next = cur
                        first_last = cur
                    else:
                        first_last = cur
                    cur = cur_next
                else:
                    cur_last = cur
                    cur = cur.next
            else:
                if first_node is None:
                    first_node = cur
                    first_last = cur_last
                cur_last = cur
                cur = cur.next
        return phead.next