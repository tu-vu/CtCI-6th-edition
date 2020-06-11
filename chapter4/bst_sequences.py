from typing import List
class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_sequences(root: TreeNode) -> List[List[int]]:
    def dfs(cur: TreeNode) -> List[List[int]]:
        if not cur:
            return [[]]
        left_seqs = dfs(cur.left)
        right_seqs = dfs(cur.right)
        cur_seqs = []
        for l_seq in left_seqs:
            for r_seq in right_seqs:
                cur_seqs.extend(weaved_seq(l_seq, r_seq, [cur.val]))
        return cur_seqs
    return dfs(root)

def weaved_seq(first: List[int], second: List[int], prefix: List[int]) -> List[List[int]]:
    if not first or not second:
        yield prefix + first + second
    else:
        yield from weaved_seq(first[1:], second, prefix + [first[0]])
        yield from weaved_seq(first, second[1:], prefix + [second[0]])