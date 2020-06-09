class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

balanced = True
def check_balanced(root: TreeNode) -> bool:
    def dfs(cur: TreeNode, depth: int) -> int:
        global balanced
        if cur:
            mx_depth_left = dfs(cur.left, depth + 1)
            mx_depth_right = dfs(cur.right, depth + 1)
            if abs(mx_depth_left - mx_depth_right) > 1:
                balanced = False
            return max(mx_depth_left, mx_depth_right)
        return depth - 1
    dfs(root, 0)
    return balanced
'''
Time complexity: O(N)
Space complexity: O(logN) from stack calls, assuming that tree is balanced so height will be logN
'''