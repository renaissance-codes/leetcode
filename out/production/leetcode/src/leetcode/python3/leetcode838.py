#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    推多米诺
"""


# 使用状态控制机制 148 ms
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp_q = []
        state = 0
        domain = []
        for i, d in enumerate(dominoes):
            domain.append(d)
            if d == "L":
                if temp_q:
                    if state == 0:
                        for q in temp_q:
                            domain[q] = "L"
                    elif state == 1:
                        tq_len = len(temp_q) // 2

                        for q in temp_q[:tq_len]:
                            domain[q] = "R"
                        for q in temp_q[::-1][:tq_len]:
                            domain[q] = "L"
                    temp_q = []
                state = 0
            elif d == "R":
                if temp_q:
                    if state == 1:
                        for q in temp_q:
                            domain[q] = "R"
                    temp_q = []
                state = 1
            else:
                temp_q.append(i)
        if state == 1 and len(temp_q):
            for q in temp_q:
                domain[q] = "R"
        return "".join(domain)