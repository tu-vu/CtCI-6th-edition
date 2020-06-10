class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def first_common_ancestor(root: TreeNode, n1: TreeNode, n2: TreeNode) -> TreeNode:
    if root: 
        if root == n1 or root == n2:
            return root
        root.left = first_common_ancestor(root.left, n1, n2)
        root.right = first_common_ancestor(root.right, n1, n2)
        if root.left and root.right:
            return root
        elif root.left:
            return root.left
        elif root.right:
            return root.right
        else:
            return None
    return None
'''
Time complexity: O(N)
Space complexity: O(N)
'''