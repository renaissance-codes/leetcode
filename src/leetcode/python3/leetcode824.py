#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    山羊拉丁文
"""


# 直接按照规则做就好了
class Solution:
    def toGoatLatin(self, S: str) -> str:
        s_split = S.split()
        vowel_set = {"a", "e", "i", "o", "u"}
        res = []
        for i, s in enumerate(s_split):
            if s[0].lower() in vowel_set:
                s = "{}ma{}".format(s, "a" * (i + 1))
            else:
                s = "{0}{1}ma{2}".format(s[1:], s[0], "a" * (i + 1))
            res.append(s)

        return " ".join(res)
