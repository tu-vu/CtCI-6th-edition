class Node:
    def __init__(self, val: int, next):
        self.val = val
        self.next = next

# Recursive version
# k starts from 1
def kth_to_last_recur(h: Node, k: int) -> None:
    if not h:
        return 0
    else:
        cnt = 1 + kth_to_last_recur(h.next, k)
        if cnt == k:
            print(h.val)
        return cnt
'''
Time complexity: O(N)
Space complexity: O(N) from stack calls
'''

# Iterative version
# k starts from 1
def kth_to_last_iter(h: Node, k: int) -> Node:
    cur, size = h, 0
    while cur:
        size += 1
        cur = cur.next
    if k > size:
        return None
    cur, cnt = h, 0
    while cur:
        if size - cnt == k:
            return cur
        cnt += 1
        cur = cur.next
    return None
'''
Time complexity:  O(N)
Space complexity: O(1) 
'''