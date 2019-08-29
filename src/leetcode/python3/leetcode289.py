#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    生命游戏
"""
from typing import List


# 按照规则来， 60ms
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        b_len = len(board)
        b_len2 = len(board[0])

        nboard = []

        for i in range(b_len):
            for j in range(b_len2):
                num = 0
                if i > 0:
                    num += board[i - 1][j]
                    if j > 0:
                        num += board[i - 1][j - 1]
                    if j < b_len2 - 1:
                        num += board[i - 1][j + 1]
                if i < b_len - 1:
                    num += board[i + 1][j]
                    if j > 0:
                        num += board[i + 1][j - 1]
                    if j < b_len2 - 1:
                        num += board[i + 1][j + 1]
                if j > 0:
                    num += board[i][j - 1]
                if j < b_len2 - 1:
                    num += board[i][j + 1]
                if board[i][j] == 1 and (num < 2 or num > 3):
                    nboard.append((i, j, 0))
                elif board[i][j] == 0 and num == 3:
                    nboard.append((i, j, 1))

        for i, j, v in nboard:
            board[i][j] = v


# 进阶使用两位来存储状态 52ms
class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r_len = len(board)
        c_len = len(board[0])

        def update(i, j):
            num = 0
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                x, y = i + x, j + y
                if x < 0 or y < 0 or x >= r_len or y >= c_len:
                    continue
                num += (board[x][y] & 1)
            if num == 2:
                board[i][j] += (board[i][j] << 1)
            elif num == 3:
                board[i][j] += 2

        for i in range(r_len):
            for j in range(c_len):
                update(i, j)

        for i in range(r_len):
            for j in range(c_len):
                board[i][j] >>= 1