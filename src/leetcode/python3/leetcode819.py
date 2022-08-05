#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    最常见的单词
"""

import re
from typing import List


# 字符串处理
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban_set = set()
        for ban in banned:
            ban_set.add(ban)

        dc = {}
        paragraph = paragraph.lower()
        paragraph = re.sub(r"[!?',;.]", " ", paragraph)
        for st in paragraph.split():
            st = st.strip()
            if not st:
                continue

            if st in ban_set:
                continue
            dc.setdefault(st, 0)
            dc[st] += 1

        dc_list = [(v, k) for k, v in dc.items()]
        dc_list.sort(key=lambda x: x[0], reverse=True)

        return dc_list[0][1]
