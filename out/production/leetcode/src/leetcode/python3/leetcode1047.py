#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    删除字符串中所有相邻重复项
"""


# 使用栈来解决问题 80ms
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return "".join(stack)
