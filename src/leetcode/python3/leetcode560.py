#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    和为k的子数组
"""
from typing import List

# 暴力求解，可惜超时不能通过
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_nums = sum(nums)
        start = 0
        end = len(nums) - 1
        result = 0
        while start <= end:
            x = 0
            for i in range(start, end + 1):
                x += nums[i]

                if x == k:
                    result += 1
                if i != end and sum_nums - x == k:
                    result += 1

            sum_nums -= (nums[start] + nums[end])
            start += 1
            end -= 1

        return result


# 使用字典搜索可能的值 152ms
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        _d = {0: 1}

        cur = 0
        for x in nums:
            cur += x
            if (cur - k) in _d:
                count += _d[cur - k]

            if cur in _d:
                _d[cur] += 1
            else:
                _d[cur] = 1

        return count