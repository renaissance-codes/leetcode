#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    用rand7()实现rand10()
"""


def rand7()->int:
    # 随机生成1-7整数
    pass


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        first = rand7()
        if first < 6:
            while True:
                second = rand7()
                if second > 5:
                    break
            res = {
                (1,6): 1,
                (1,7): 2,
                (2,6): 3,
                (2,7): 4,
                (3,6): 5,
                (3,7): 6,
                (4,6): 7,
                (4,7): 8,
                (5,6): 9,
                (5,7): 10
            }
            return res[(first, second)]
        else:
            while True:
                second = rand7()
                if second < 6:
                    break
            res = {
                (6,1): 1,
                (7,2): 2,
                (6,3): 3,
                (7,4): 4,
                (6,5): 5,
                (7,1): 6,
                (6,2): 7,
                (7,3): 8,
                (6,4): 9,
                (7,5): 10
            }
            return res[(first, second)]
