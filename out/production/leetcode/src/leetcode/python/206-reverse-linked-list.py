#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author  :   https://github.com/xixici
Date    :   2019/8/22
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     ln = None
    #     while head:
    #         lt = head.next
    #         head.next = ln
    #         ln = head
    #         head = lt
    #     return ln
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ln = None
        return self.reverse(head, ln)

    def reverse(self, head, ln):
        if head is None:
            return ln
        lt = head.next
        head.next = ln
        return self.reverse(lt, head)
