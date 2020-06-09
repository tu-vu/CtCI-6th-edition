class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validate_bst(root: TreeNode):
    def dfs(cur: TreeNode, mx=float('inf'), mn=float('-inf')) -> bool:
        if cur: 
            return mn <= cur.val < mx and dfs(cur.left, cur.val, mn) and dfs(cur.right, mx, cur.val)
        return True
    return dfs(root)
'''
Time complexity: O(N)
Space complexity: O(logN) from stack calls, assuming that tree is balanced so height will be logN
'''