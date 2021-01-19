#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    字符串解码
"""


# 使用栈暴力破解 44ms
class Solution:
    def decodeString(self, s: str) -> str:
        numstack = []

        for si in s:
            if si.isdigit():
                if numstack and numstack[-1].isdigit():
                    p = numstack.pop()
                    p += si
                    numstack.append(p)
                else:
                    numstack.append(si)
            elif si == "[":
                numstack.append(si)
            elif si.isalpha():
                if numstack and numstack[-1].isalpha():
                    p = numstack.pop()
                    p += si
                    numstack.append(p)
                else:
                    numstack.append(si)
            else:
                res = ""
                p = numstack.pop()
                while p != "[":
                    if p.isalpha():
                        res = p + res
                    else:
                        res *= int(res)
                    p = numstack.pop()
                if numstack[-1].isdigit():
                    p = numstack.pop()
                    res *= int(p)
                numstack.append(res)
        ans = "".join(numstack)
        return ans


class Solution2:
    def decodeString(self, s: str) -> str:
        numstack = []
        num = 0
        lst = ""
        for si in s:
            if si.isdigit():
                num = num * 10 + int(si)
            elif si == "[":
                numstack.append((lst, num))
                lst, num = "", 0
            elif si.isalpha():
                lst += si
            else:
                lstr, lnum = numstack.pop()
                lst = lstr + lst * lnum

        return lst
