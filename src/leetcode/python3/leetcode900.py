#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    RLE迭代器
"""
from typing import List


class RLEIterator:

    def __init__(self, A: List[int]):
        self.data = [(A[2*i+1], x) for i, x in enumerate(A[::2])][::-1]

    def next(self, n: int) -> int:
        while self.data:
            x, d = self.data.pop()
            if n > d:
                n -= d
            else:
                if d > n:
                    self.data.append((x, d-n))
                return x
        return -1


# 使用位置计数
class RLEIterator2:

    def __init__(self, A: List[int]):
        self.data = A
        self.i = 0
        self.q = 0

    def next(self, n: int) -> int:
        while self.i < len(self.data):
            if self.q + n <= self.data[self.i]:
                self.q += n
                return self.data[self.i + 1]
            else:

                n -= self.data[self.i] - self.q
                self.i += 2
                self.q = 0

        return -1
