from functools import lru_cache


class Solution:
    def minSteps(self, n: int) -> int:

        @lru_cache(None)
        def dp(i):
            if i == 1:
                return 0
            elif i == 2:
                return 2
            else:
                for j in range(2, i - 1):
                    if i % j == 0:
                        return (dp(int(i / j)) + j)
                return i

        return dp(n)
