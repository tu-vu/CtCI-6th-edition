class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def intersection(h1: Node, h2: Node) -> Node:
    cur1, cur2 = h1, h2
    last1 = last2 = shorter = longer = None
    length1 = length2 = 0
    while cur1:
        length1 += 1
        if not cur1.next:
            last1 = cur1
        cur1 = cur1 .next
    while cur2:
        length2 += 1
        if not cur2.next:
            last2 = cur2
        cur2 = cur2.next
    if length1 == 0 or length2 == 0 or last1 != last2:
        return None 
    if length1 < length2:
        shorter = h1
        longer = h2
    else:
        shorter = h2
        longher = h1
    for i in range(abs(length1 - length2)):
        longer = longer.next
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return shorter
'''
Intuition: Make two lists equal in term of length, then traverse both list at same time. The first encountered node they share is the answer
Time complexity: O(A + B)
Space complexitY: O(1)
'''