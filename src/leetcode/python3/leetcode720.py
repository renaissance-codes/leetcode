#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    词典中最长的单词
"""
from typing import List


class Node(object):

    def __init__(self):
        self.value = None
        self.is_root = False
        self.next = {}


class Solution:
    # 先排序
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: len(x))

        root = Node()
        root.is_root = True
        max_res = ""
        for word in words:
            trt = root
            is_subs = True
            for w in word:
                if not trt.is_root:
                    is_subs = False
                    break

                if w not in trt.next:
                    trt.next[w] = Node()
                    trt = trt.next[w]
                else:
                    trt = trt.next[w]
                    # is_subs.append(trt.is_root)

            if is_subs:
                if len(word) > len(max_res):
                    max_res = word
                elif len(word) == len(max_res):
                    max_res = min(word, max_res)
                trt.is_root = True

        return max_res


# 广度优先
class Solution2:
    def longestWord(self, words: List[str]) -> str:

        root = Node()
        # root.val = ""
        root.is_root = True
        for word in words:
            trt = root
            for w in word:
                if w not in trt.next:
                    trt.next[w] = Node()
                trt = trt.next[w]
            trt.is_root = True
            trt.val = word

        queue_list = [root]
        max_res = ""
        while len(queue_list):
            nq = []
            for q in queue_list:
                if q.is_root:
                    if len(q.val) > len(max_res):
                        max_res = q.val
                    elif len(q.val) == len(max_res):
                        max_res = min(max_res, q.val)
                    for _, tq in q.next.items():
                        nq.append(tq)
            queue_list = nq

        return max_res


# 116ms  设计非常巧妙
class Solution3:
    def longestWord(self, words: List[str]) -> str:

        words.sort()
        s_set = set()
        res = ""
        for word in words:
            if word[:-1] in s_set or word[:-1] == "":
                if len(word) > len(res):
                    res = word
                s_set.add(word)
        return res
