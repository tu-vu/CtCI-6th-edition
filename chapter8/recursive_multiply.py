from typing import Dict
import collections
def recursive_multiply(A: int, B: int) -> int:
    def dp(A: int, B: int, memo: Dict[int, int]) -> int:
        if B == 1:
            return A
        if memo[B] == 0:
            half = B >> 1
            memo[B] = dp(A, half, memo) + dp(A, B - half, memo)
        return memo[B]
    memo = collections.defaultdict(int)
    return dp(A, B, memo)