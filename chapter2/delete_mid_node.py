class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def delete_mid_node(target: Node):
    while target:
        target.val = target.next.val
        if not target.next.next:
            target.next = None
        target = target.next
'''
Intuition: Simple copy val from next and delete last element
Time complexity: O(N)
Space complexity: O(1)
'''