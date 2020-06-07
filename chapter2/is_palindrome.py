class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def is_palindrome(h: Node) -> bool:
    def reverse(cur: Node, prev: Node) -> Node:
        cpy = Node(cur.val)
        cpy.next = prev
        if not cur.next:
            return cpy
        else:
            return reverse(cur.next, cpy)
    if not h:
        return False
    reversed = reverse(h, None)
    ok = True
    while h or reversed:
        if not h or not reversed or h.val != reversed.val:
            ok = False
            break
        h = h.next
        reversed = reversed.next
    return ok
'''
Intuition: Reverse the linked list then compare
Time complexity: O(N)
Space complexity: O(N) from stack calls
'''