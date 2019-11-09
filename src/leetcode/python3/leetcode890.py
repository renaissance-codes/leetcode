#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    查找和基础模式
"""
from typing import List


# 两个字典作为映射查找
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        result = []
        for wd in words:
            d = {}
            r = {}

            ispass = 1
            for i, w in enumerate(wd):
                key = pattern[i]
                if key not in d and w not in r:
                    d[key] = w
                    r[w] = key
                else:
                    if d.get(key, "") != w or r.get(w) != key:
                        ispass = 0
                        break

            if ispass:
                result.append(wd)

        return result
