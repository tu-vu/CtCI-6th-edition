class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def remove_dups(h: Node) -> Node:
    container, cur, prev = set(), h, None
    while cur:
        # If val already in container, remove it
        if cur.val in container:
            if not prev:
                h = cur.next
                cur = h
            else:
                prev.next = cur.next
                cur = cur.next
        else:
            container.add(cur.val)
            prev = cur
            cur = cur.next
    return h
'''
Time complexity:  O(N)
Space complexity: O(N)
'''