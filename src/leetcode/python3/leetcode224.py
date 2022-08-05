#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    模拟简单计算器
"""


# 使用stack来处理， 244ms
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for se in s:
            if se == " ":
                continue

            if len(stack) == 0:
                if se.isdigit():
                    stack.append(int(se))
                else:
                    stack.append(se)
            else:
                if se.isdigit():
                    if isinstance(stack[-1], int):
                        x = stack.pop()
                        x = x * 10 + int(se)
                        stack.append(x)
                    else:
                        stack.append(int(se))
                else:
                    if se in ["+", "-"]:
                        self.update_stack(stack)
                        stack.append(se)
                    elif se == ")":
                        self.update_stack(stack)
                        x = stack.pop()
                        left_s = stack.pop()
                        stack.append(x)
                        self.update_stack(stack)
                    else:
                        stack.append(se)
        while len(stack) > 1:
            self.update_stack(stack)
        return stack[0]

    def update_stack(self, stack):
        x = stack.pop()
        if len(stack) and stack[-1] in ["-", "+"]:
            sign = stack.pop()
            y = stack.pop()
            if sign == "+":
                x += y
            else:
                x = y - x
        stack.append(x)


# 最简单的方法，使用eval方法, 会有内存问题，通不过测试
class Solution2:
    def calculate(self, s: str) -> int:
        return eval(s)
