#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    回文链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 逆转一半的链表，然后比较 84ms
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        hlen = 0
        nhead = head
        while nhead:
            nhead = nhead.next
            hlen += 1
        if hlen < 2:
            return True

        tail = None
        nhead = head
        for _ in range(hlen // 2):
            ht = nhead.next
            nhead.next = tail
            tail = nhead
            nhead = ht

        if hlen % 2:
            nhead = nhead.next

        for i in range(hlen // 2):
            if nhead.val != tail.val:
                return False
            nhead = nhead.next
            tail = tail.next
        return True