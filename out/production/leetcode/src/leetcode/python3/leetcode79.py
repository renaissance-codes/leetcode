#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    单词搜索
"""
from typing import List


# 深度优先
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_r = len(board)
        board_c = len(board[0])

        if len(word) == 0:
            return True

        d = []
        for i in range(board_r):
            for j in range(board_c):
                alpha = board[i][j]
                if word[0] == alpha:
                    d.append((i, j))
        if len(d) == 0:
            return False

        def wordsearch(loc, alpha, path):
            i, j = loc
            change = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            res = []
            for xi, yi in change:
                if xi + i < 0 or xi + i >= board_r or yi + j < 0 or yi + j >= board_c:
                    continue

                if (xi + i, yi + j) in path:
                    continue
                if alpha == board[xi + i][yi + j]:
                    res.append((xi + i, yi + j))
            return res

        def wordexist(loc, inputword, sset):
            if len(inputword) == 0:
                return True
            res = wordsearch(loc, inputword[0], sset)

            ans = 0
            for i, j in res:
                if wordexist((i, j), inputword[1:], sset | {(i, j)}):
                    ans = 1
                    break

            return ans

        ans = 0
        for x, y in d:
            if wordexist((x, y), word[1:], {(x, y)}):
                ans = 1
                break

        return ans
