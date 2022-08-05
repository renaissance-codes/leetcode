#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author  :   https://github.com/xixici
Date    :   2019/8/24
"""


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for word in words:
            c = list(chars)
            flag = 1
            wordS = list(word)
            for w in wordS:
                if w in c:
                    c.remove(w)
                else:
                    flag = 0
            if flag == 1:
                res += len(wordS)
        return res
