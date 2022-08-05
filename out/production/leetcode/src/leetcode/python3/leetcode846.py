#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 直观解法
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W == 1:
            return True

        h_dict = dict()

        for h in hand:
            h_dict.setdefault(h, 0)
            h_dict[h] += 1

        nums = list(h_dict.keys())
        nums.sort()
        if len(nums) < W:
            return False

        all_num = 0
        for n in nums:
            n_num = h_dict[n]
            if n_num == 0:
                continue

            for i in range(W):
                if h_dict.get(n + i, 0) < n_num:
                    return False
                h_dict[n + i] -= n_num
            all_num += n_num * W
        if all_num != len(hand):
            return False

        return True
