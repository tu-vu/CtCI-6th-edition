from typing import List
import collections
def triple_step(n: int) -> int:
    def dp(n: int, memo: List[int]) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        if memo[n] == 0:
            memo[n] = dp(n - 1, memo) + dp(n - 2, memo) + dp(n - 3, memo)
        return memo[n]
    memo = collections.defaultdict(int)
    return dp(n, memo)
'''
Time complexity: O(n)
Space complexity: O(n)
'''