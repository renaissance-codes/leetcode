#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    石子游戏
"""
from typing import List

# 无论是怎样的石子，先拿的肯定赢
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# 使用动态规划求解
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        d_len = len(piles)
        dp = [[[0, 0] for j in range(d_len)] for i in range(d_len)]

        for i in range(d_len):
            dp[i][i][0] = piles[i]

        for g in range(2, d_len + 1):
            for i in range(d_len - g + 1):
                left = piles[i] + dp[i + 1][i + g - 1][0]
                right = piles[i + g - 1] + dp[i][i + g - 2][0]

                if left > right:
                    dp[i][i + g - 1][0] = left
                    dp[i][i + g - 1][1] = dp[i + 1][i + g - 1][0]
                else:
                    dp[i][i + g - 1][0] = right
                    dp[i][i + g - 1][1] = dp[i][i + g - 2][0]

        return dp[0][d_len - 1][0] > dp[0][d_len - 1][1]



from functools import lru_cache
# 动态规划思路2
class Solution3:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0
