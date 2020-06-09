from typing import List
import collections
class TreeNode:
    def __init__(self, val: int, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def list_of_depths(root: TreeNode) -> List[TreeNode]:
    res = []
    def bfs(root: TreeNode, res: List[TreeNode]) -> None:
        q = collections.deque()
        q.append(root)
        while q:
            ori_length, cur = len(q), None
            for _ in range(ori_length):
                removed = q.popleft()
                if not cur:
                    cur = TreeNode(removed.val)
                    res.append(cur)
                else:
                    cur.next = TreeNode(removed.val)
                    cur = cur.next
                if removed.left:
                    q.append(removed.left)
                if removed.right:
                    q.append(removed.right)

    bfs(root, res)
    return res
'''
Time complextiy: O(N)
Space complexity: O(N) for queue
'''