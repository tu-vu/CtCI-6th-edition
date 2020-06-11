from typing import List
import copy
class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def paths_with_sum(root: TreeNode, key: int) -> int:
    def dfs(cur: TreeNode, prefix: List[int], key: int) -> int:
        if not cur:
            return 0
        cpy = copy.deepcopy(prefix)
        cpy.append(0)
        cpy = [pre_sum + cur.val for pre_sum in cpy]
        cnt_valid = sum(1 if sum == key else 0 for sum in cpy)
        return cnt_valid + dfs(cur.left, cpy, key) + dfs(cur.right, cpy, key)
    return dfs(root, [], key)