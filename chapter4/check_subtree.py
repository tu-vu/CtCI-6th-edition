class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_subtree(r1: TreeNode, r2: TreeNode) -> bool:
    if not r1:
        return False
    if r1.val == r2.val and is_valid(r1, r2):
        return True
    return check_subtree(r1.left, r2) or check_subtree(r1.right, r2)

def is_valid(r1: TreeNode, r2: TreeNode) -> bool:
    if r1 and r2:
        return r1.val == r2.val and is_valid(r1.left, r2.left) and is_valid(r1.right, r2.right)
    elif not r1 and not r2:
        return True
    return False
'''
Time complexity: O(N * M)
Space complexity: O(log(N) + log(M))
'''