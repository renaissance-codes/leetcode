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


# 使用深度优先策略 412ms
class WordDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tempt_root = self.root
        for s in word:
            if s not in tempt_root:
                tempt_root[s] = dict()
            tempt_root = tempt_root[s]
        if "$" not in tempt_root:
            tempt_root["$"] = dict()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        tempt_root = self.root

        def dfs(input_s, iroot):
            if len(input_s) == 0:
                if "$" in iroot:
                    return True
                return False

            fs = input_s[0]
            if fs == ".":
                result = []
                for _, v in iroot.items():
                    result.append(dfs(input_s[1:], v))
                return any(result)
            elif fs in iroot:
                return dfs(input_s[1:], iroot[fs])
            else:
                return False

        return dfs(word, tempt_root)

# 按照字符串长度进行分类比较 188ms
from collections import defaultdict
class WordDictionary3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        n_len = len(word)
        self.root[n_len].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        t_len = len(word)

        for wd in self.root[t_len]:
            result = 0
            for i, s in enumerate(word):
                if s == "." or wd[i] == s:
                    result += 1
                else:
                    break
            if result == t_len:
                return True

        return False