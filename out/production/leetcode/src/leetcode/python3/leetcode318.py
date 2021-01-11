#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    最大单词长度乘积
"""
from typing import List


# 利用26位进行判别是否有重合地方,444ms
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dlen = len(words)
        word_value = [0] * dlen
        start = ord("a")
        for i, word in enumerate(words):
            wv = 0
            for w in set(word):
                wv += 1 << (ord(w) - start)
            word_value[i] = wv

        ans = 0
        for i in range(dlen - 1):
            for j in range(i + 1, dlen):
                if word_value[i] & word_value[j]:
                    continue
                ans = max(len(words[i]) * len(words[j]), ans)

        return ans


# 优化数据结构，使用dict存储相同字符集合的长度
class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        start = ord("a")
        d = {}
        for i, word in enumerate(words):
            wv = 0
            for w in set(word):
                wv += 1 << (ord(w) - start)
            d[wv] = max(d.get(wv, 0), len(word))

        ans = 0
        for k, v in d.items():
            for m, n in d.items():
                if k & m:
                    continue
                if v * n > ans:
                    ans = v * n

        return ans
