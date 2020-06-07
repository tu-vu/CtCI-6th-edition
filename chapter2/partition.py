class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def partition(h: Node, x: int) -> Node:
    less, greater, end_less, end_greater, cur = None, None, None, None, h
    while cur:
        if cur.val < x:
            if not less:
                less = Node(cur.val)
                end_less = less
            else:
                end_less.next = Node(cur.val)
                end_less = end_less.next
        else:
            if not greater:
                greater = Node(cur.val)
                end_greater = greater
            else:
                end_greater.next = Node(cur.val)
                end_greater = end_greater.next
        cur = cur.next
    end_less.next = greater
    return less

'''
Intuition: Partition operation in Quick Sort, but now using linked list!
Time complexity: O(N)
Space complexity: O(N)
'''