#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    为运算表达式设计优先级
"""
from typing import List


# 使用动态规划，从底至上 44ms
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        num_list = []
        operate = []
        t = ""
        for s in input:
            if s.isdigit():
                t += s
            else:
                num_list.append(int(t))
                t = ""
                operate.append(s)

        def get_op(n1, n2, op):
            if op == "+":
                return n1 + n2
            elif op == "-":
                return n1 - n2
            else:
                return n1 * n2

        num_list.append(int(t))

        if not operate:
            return num_list

        d_len = len(num_list)
        d_list = {(i, i + 1): [get_op(num_list[i], num_list[i + 1], operate[i])] for i in range(d_len - 1)}
        for i in range(2, d_len):
            print(d_list)
            for j in range(d_len - i):
                tlist = []
                for k in range(j, j + i):
                    if k == j:
                        for v in d_list[(j + 1, j + i)]:
                            tlist.append(get_op(num_list[j], v, operate[j]))
                    elif k == j + i - 1:
                        for v in d_list[(j, j + i - 1)]:
                            tlist.append(get_op(v, num_list[j + i], operate[j + i - 1]))
                    else:
                        v1 = d_list[(j, k)]
                        v2 = d_list[(k + 1, j + i)]

                        for t1 in v1:
                            for t2 in v2:
                                tlist.append(get_op(t1, t2, operate[k]))
                d_list[(j, j + i)] = tlist
        return d_list[(0, d_len - 1)]


# 不分割字符串 52ms
class Solution2:
    def diffWaysToCompute(self, input: str) -> List[int]:

        d_dict = {}

        def partition(input_str):
            if "+" not in input_str and "-" not in input_str and "*" not in input_str:
                return [int(input_str)]
            result = []
            for i, x in enumerate(input_str):
                if x in ["*", "-", "+"]:
                    if input_str[:i] in d_dict:
                        left = d_dict[input_str[:i]]
                    else:
                        left = partition(input_str[:i])
                        d_dict[input_str[:i]] = left
                    if input_str[i + 1:] in d_dict:
                        right = d_dict[input_str[i + 1:]]
                    else:
                        right = partition(input_str[i + 1:])
                        d_dict[input_str[i + 1:]] = right
                    for lf in left:
                        for rg in right:
                            if x == "*":
                                result.append(lf * rg)
                            elif x == "-":
                                result.append(lf - rg)
                            else:
                                result.append(lf + rg)
            return result

        return partition(input)
