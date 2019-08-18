#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    字符串最大公因子
"""


# 思路，先求字符串长度的最大公因子，然后验证这个最大公因子长度的字符串是否是字符串公因子 56ms
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        first_len = len(str1)
        second_len = len(str2)

        if first_len == 0 or second_len == 0:
            return ""

        big_one = max(first_len, second_len)
        pub_num = min(first_len, second_len)
        while big_one % pub_num:
            mod = big_one % pub_num
            big_one = pub_num
            pub_num = mod

        def check(s, spart):
            if spart == "":
                return True
            for si in range(pub_num):
                if s[si] != spart[si]:
                    return False
            return check(s, spart[pub_num:])

        smod = str1[:pub_num]

        if check(smod, str1) and check(smod, str2):
            return smod
        return ""
