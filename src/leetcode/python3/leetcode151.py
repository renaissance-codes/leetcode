#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    翻转字符串里的单词
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = ""
        res = []
        for x in s:
            if x == " ":
                if tmp:
                    res.append(tmp)
                    tmp = ""
            else:
                tmp += x

        if tmp:
            res.append(tmp)

        return " ".join(res[::-1])
