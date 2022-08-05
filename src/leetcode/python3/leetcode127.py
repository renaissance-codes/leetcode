#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    单词接龙
"""
from typing import List


# 通过比较相似字符串
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d_dict = dict()
        for x in wordList:
            wq = list(x)
            for i, w in enumerate(x):
                wq[i] = "*"
                key = "".join(wq)
                d_dict.setdefault("".join(key), [])
                d_dict[key].append(x)
                wq[i] = w

        sset = set()
        queue = [beginWord]
        deep = 1
        while queue:
            n_q = []
            for q in queue:
                if q in sset:
                    continue
                sset.add(q)
                if q == endWord:
                    return deep
                wq = list(q)
                for i, x in enumerate(q):
                    wq[i] = "*"
                    key = "".join(wq)
                    if key in d_dict:
                        n_q += d_dict[key]
                    wq[i] = q[i]

            deep += 1
            queue = n_q

        return 0


# 双向广度优先
class Solution2:

    def visit(self, uqueue, ddict, oqueue, sset, deep):
        v = 0
        n_q = []
        for q in uqueue:
            if q in sset:
                continue
            sset.add(q)
            if q in oqueue:
                v = deep
                break
            for i in range(len(q)):
                key = q[:i] + "*" + q[i + 1:]
                if key in ddict:
                    n_q += ddict[key]

        uqueue = n_q

        return v, uqueue

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        w_len = len(beginWord)
        d_dict = dict()
        for x in wordList:
            for i in range(w_len):
                key = x[:i] + "*" + x[i + 1:]
                d_dict.setdefault(key, [])
                d_dict[key].append(x)

        sset = set()
        queue = [beginWord]
        oqueue = [endWord]
        deep = 1
        while queue and oqueue:

            ans, queue = self.visit(queue, d_dict, oqueue, sset, deep)
            if ans:
                return ans
            deep += 1

            ans, oqueue = self.visit(oqueue, d_dict, queue, sset, deep)
            if ans:
                return ans
            deep += 1

        return 0
