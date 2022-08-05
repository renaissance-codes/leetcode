#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    标签验证器
"""


class Solution:
    def isValid(self, code: str) -> bool:
        if len(code) > 1 and code[1] == "!":
            return False
        big_set = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                   "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

        def is_valid_tag(input_str):
            if len(input_str) < 1 or len(input_str) > 9:
                return False
            for x in input_str:
                if x not in big_set:
                    return False
            return True

        flag = 0
        cdf = ""
        tag_content = ""
        tag_name = ""
        cdata = ""
        stack_tag = []
        has_tag = 0
        for i, x in enumerate(code):
            if flag == 0:
                if x == "<":
                    flag = 1
                else:
                    return False
            elif flag == 1:
                if x == "<":
                    return False
                elif x == ">":
                    if not is_valid_tag(tag_name):
                        return False
                    stack_tag.append(tag_name)
                    tag_name = ""
                    has_tag += 1
                    flag = 2
                else:
                    tag_name += x

                    if tag_name[0] == "!":
                        flag = 4
                        cdf = "[CDATA["
                        tag_name = ""
                    elif tag_name[0] == "/":
                        flag = 3
                        tag_name = ""

            elif flag == 2:
                if x == "<":
                    flag = 1
                else:
                    tag_content += x
            elif flag == 3:
                if x == ">":
                    if not is_valid_tag(tag_name):
                        return False
                    if len(stack_tag) == 0:
                        return False
                    if stack_tag[-1] != tag_name:
                        return False
                    stack_tag.pop()

                    if len(stack_tag) == 0 and i != len(code) - 1:
                        return False

                    tag_name = ""
                    flag = 2
                else:
                    tag_name += x
            else:
                if len(cdf):
                    if cdf[0] == x:
                        cdf = cdf[1:]
                    else:
                        return False
                else:
                    cdata += x
                    if len(cdata) >= 3 and cdata[-3:] == "]]>":
                        flag = 2
                        cdata = ""

        return len(stack_tag) == 0 and has_tag
