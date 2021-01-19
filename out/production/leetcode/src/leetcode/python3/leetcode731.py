#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    我的日程安排II
"""

# 非常直观的思路，但是超时
class MyCalendarTwo:

    def __init__(self):
        self.w = []

    def book(self, start: int, end: int) -> bool:
        if not self.w:
            self.w = [(start, 1), (end, -1)]
            return True

        start_i = None
        end_i = None
        i = 0
        t = 0
        # print(start, end, self.w)
        while i < len(self.w) and (self.w[i][0] <= start or self.w[i][0] < end):
            # print(t, i, self.w[i])
            if start_i is None and self.w[i][0] > start:
                start_i = i
                if t == 2:
                    return False
            if end_i is None and self.w[i][0] >= end:
                end_i = i

            if start_i is not None:
                if t == 2:
                    return False
            t += self.w[i][1]

            i += 1

        if start_i is None:
            start_i = i
            if t == 2:
                return False

        if end_i is None:
            end_i = i
            if t == 2:
                return False

        self.w.insert(start_i, (start, 1))
        self.w.insert(end_i + 1, (end, -1))

        return True


# 建立两个数组，一个是出现一次，一个是出现两次，问题想复杂了 524ms
class MyCalendarTwo2:

    def __init__(self):
        self.first = []
        self.second = []

    def book(self, start: int, end: int) -> bool:
        if not self.first:
            self.first = [(start, end)]
            return True

        for x, y in self.second:
            if start >= y or end <= x:
                continue
            return False

        for x, y in self.first:
            if start >= y or end <= x:
                continue
            self.second.append((max(start, x), min(end, y)))

        self.first.append((start, end))

        return True