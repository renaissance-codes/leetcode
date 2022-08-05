#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 构建索引列表
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def order_data():
            index = []
            for i, d in enumerate(logs):
                d_split = d.split(" ")
                if d_split[1].isdigit():
                    index.append((1, i, i))
                else:
                    index.append((0, " ".join(d_split[1:] + d_split[:1]), i))
            index.sort(key=lambda x: (x[0], x[1]))

            for x, y, i in index:
                yield logs[i]

        return [log for log in order_data()]
