#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
添加和搜索单词
"""


# 使用类似于trie 树的dict结构来存储单词，248ms, 改进的话需要使用ac自动机
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tempt_root = self.root
        for s in word:
            if s not in tempt_root:
                tempt_root[s] = {}
            tempt_root = tempt_root[s]
        if "$" not in tempt_root:
            tempt_root["$"] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        tempt_root = self.root
        queue = [tempt_root]
        for s in word:
            n_queue = []
            for q in queue:
                if s == ".":
                    n_queue += q.values()
                elif s in q:
                    n_queue.append(q[s])

            if len(n_queue):
                queue = n_queue
            else:
                return False
        for q in queue:
            if "$" in q:
                return True
        return False