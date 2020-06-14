from typing import Dict
from typing import List
import collections
res = []
def robot_in_grid(board: List[List[bool]], r: int, c: int) -> List[List[int]]:
    def dp(x: int, y: int, r: int, c: int, memo: Dict[List[List[int]], bool]) -> bool:
        global res
        # If out of bound or blocked
        if x >= c or y >= r or not board[y][x]:
            return False
        # If at destination
        if x == c - 1 and y == r - 1:
            return True
        if memo[(x,y)] is None:
            memo[(x,y)] = dp(x + 1, y, r, c, memo) or dp(x, y + 1, r, c, memo)
        if memo[(x,y)]:
            res = [[y, x]] + res
            return True
        return False  
    memo = collections.defaultdict(lambda: None)
    if dp(0, 0, r, c, memo):
        return res + [[r-1, c-1]]
    print("Unavailable valid path!")
'''
Time complexity: O(rc)
Space complexity: O(max(r,c)) from stack calls
'''