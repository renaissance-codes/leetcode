#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    比较含退格的字符串
"""


# 使用栈来处理
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sstack = []
        tstack = []

        for s in S:
            if s == "#":
                if len(sstack):
                    sstack.pop()
            else:
                sstack.append(s)

        for s in T:
            if s == "#":
                if len(tstack):
                    tstack.pop()
            else:
                tstack.append(s)

        return sstack == tstack


# 双指针的故事
class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sind = len(S) - 1
        tind = len(T) - 1
        scou = 0
        tcou = 0

        while sind >= 0 or tind >= 0:
            while sind >= 0 and (S[sind] == "#" or scou > 0):
                if S[sind] == "#":
                    scou += 1
                else:
                    scou = scou - 1 if scou > 0 else 0
                sind -= 1
            while tind >= 0 and (T[tind] == "#" or tcou > 0):
                if T[tind] == "#":
                    tcou += 1
                else:
                    tcou = tcou - 1 if tcou > 0 else 0
                tind -= 1

            if sind < 0 and tind < 0:
                return True
            elif sind < 0 or tind < 0:
                return False

            if S[sind] != T[tind]:
                return False
            sind -= 1
            tind -= 1
        if sind < 0 and tind < 0:
            return True
        else:
            return False
