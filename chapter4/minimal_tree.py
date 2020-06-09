from typing import List
class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimal_tree(arr: List[int]) -> TreeNode:
    def build_tree(arr: List[int], lo: int, hi: int) -> TreeNode:
        if lo <= hi:
            mid = (lo + hi) // 2
            cur = TreeNode(arr[mid])
            cur.left = build_tree(arr, lo, mid - 1)
            cur.right = build_tree(arr, mid + 1, hi)
            return cur
    return build_tree(arr, 0, len(arr) - 1)
'''
Time complexity: O(N)
Space complexity: O(N) from stack calls
'''