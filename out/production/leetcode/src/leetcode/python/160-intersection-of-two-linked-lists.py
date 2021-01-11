#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author  :   https://github.com/xixici
Date    :   2019/8/21
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :param headB:
        :param headA:
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while pa != pb:
            # if pa is not None:
            #     pa = pa.next
            # else:
            #     pa = headB
            pa = pa.next if pa is not None else headB
            if pb is not None:
                pb = pb.next
            else:
                pb = headA
        return pa
