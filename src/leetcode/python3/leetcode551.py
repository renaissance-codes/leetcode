#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    学生出勤记录
"""


# 简单思路
class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_state = 0
        for x in s:
            if x == "A":
                a_count += 1
                l_state = 0
            elif x == "L":
                l_state += 1
                if l_state > 2:
                    return False
            else:
                l_state = 0
        if a_count > 1:
            return False

        return True


# 简介代码
class Solution2:
    def checkRecord(self, s: str) -> bool:
        return s.count("A") < 2 and s.count("LLL") < 1
