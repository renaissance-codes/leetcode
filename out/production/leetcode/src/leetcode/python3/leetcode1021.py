#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    删除最外部的括号
"""

# 使用栈
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        v = 0
        result = ""
        for s in S:
            if s == "(":
                stack.append(s)
                v += 1
            else:
                if v>1:
                    stack.append(s)
                    v -= 1
                else:
                    result += "".join(stack[1:])
                    stack = []
                    v = 0
        return result


# 只需要计数器就可以了， 52ms
class Solution2:
    def removeOuterParentheses(self, S: str) -> str:
        v = 0
        result = ""
        if len(S) < 1:
            return result
        for s in S:
            if s == "(":
                if v != 0:
                    result += "("
                v += 1
            else:
                if v>1:
                    result += ")"
                v -= 1
        return result