class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

res = None
def successor(root: TreeNode, target: int) -> TreeNode:
    def dfs(cur: TreeNode, target: int, parent: TreeNode) -> TreeNode:
        global res
        if cur:
            next_cur = dfs(cur.right, target, parent)
            if cur.val == target:
                res = next_cur if next_cur else parent
            next_prev = dfs(cur.left, target, cur)
            # if there's leftmost node return it, else return cur node
            return next_prev if next_prev else cur
        return None
    dfs(root, target, None)
    return res
'''
Time complexity: O(N)
Space complexity: O(logN) from stack calls, assuming that tree is balanced so height will be logN
'''