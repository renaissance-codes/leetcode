#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    将字符串转化为数字
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        state = 0
        num = 0
        for s in str:
            if state == 0:
                if s == "-":
                    sign = -1
                    first = False
                    state = 1
                elif s == "+":
                    sign = 1
                    first = False
                    state = 1
                elif s.isdigit():
                    num = int(s)
                    state = 1
                elif s == " ":
                    continue
                else:
                    break
            elif state == 1:
                if s.isdigit():
                    num = num*10 + int(s)
                else:
                    break
        if sign == 1:
            if num > (1<<31)-1:
                return (1<<31)-1
        else:
            if num > 1<<31:
                return -1*(1<<31)
        return sign * num