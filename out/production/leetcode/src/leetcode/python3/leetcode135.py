#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    分糖果
"""
from typing import List


# 直观的解法， 比较局部高点两边的结果，
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return len(ratings)

        state = []

        num = 0

        def calculate_data(last_c):

            rnum = 0
            sub_num = 0
            init = -1

            if base == 1:
                q = state.pop()

                while len(state):
                    x = state.pop(0)
                    if x > init:
                        sub_num += 1
                    else:
                        sub_num = 1
                    init = x
                    rnum += sub_num
                if q == init:
                    sub_num = 1
                else:
                    sub_num += 1
                state.append(q)
            else:
                sub_num = 1
                q = state.pop()

                init = q
                while len(state):
                    x = state.pop()
                    if x > init:
                        sub_num += 1
                    else:
                        sub_num = 1
                    init = x
                    rnum += sub_num
                if last_c > sub_num:
                    rnum += last_c - sub_num
                state.append(q)

            return rnum, sub_num

        base = 0
        last_count = -1
        for x in ratings:
            if len(state):
                # 状态判断
                if state[-1] < x:
                    if base == -1:
                        rnum, last_v = calculate_data(last_count)
                        num += rnum
                    base = 1
                elif state[-1] > x:
                    if base == 1:
                        rnum, last_v = calculate_data(0)
                        num += rnum
                        last_count = last_v
                    base = -1

            state.append(x)
        if base == 1:
            init = -1
            sub_num = 0
            for x in state:

                if x > init:
                    sub_num += 1
                elif x == init:
                    sub_num = 1
                init = x
                num += sub_num
        elif base == -1:
            init = -1
            sub_num = 0
            while len(state):
                x = state.pop()
                if x > init:
                    sub_num += 1
                elif x == init:
                    sub_num = 1
                init = x
                num += sub_num
            if last_count > sub_num:
                num += last_count - sub_num
        else:
            num += len(state)

        return num


# 左右扫描，然后比较
class Solution2:
    def candy(self, ratings: List[int]) -> int:
        d_rating = len(ratings)
        if d_rating < 2:
            return d_rating

        state = [1] * d_rating
        init = ratings[0]
        for i in range(1, d_rating):
            if ratings[i] > init:
                state[i] = state[i - 1] + 1
            init = ratings[i]
        init = ratings[d_rating - 1]
        for j in range(d_rating - 2, -1, -1):
            if ratings[j] > init:
                if j == 0:
                    state[j] = state[j + 1] + 1
                else:
                    if ratings[j] > ratings[j - 1]:
                        state[j] = max(state[j + 1], state[j - 1]) + 1
                    else:
                        state[j] = state[j + 1] + 1
            init = ratings[j]

        return sum(state)