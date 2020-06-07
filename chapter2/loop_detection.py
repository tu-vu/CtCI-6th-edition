class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def loop_detection(h: Node) -> Node:
    # Declare a HashSet which allows for O(1) membership checking
    container = set()
    while h:
        if h in container:
            return h
        container.add(h)
        h = h.next
    return None
'''
Time complexity: O(N)
Space complexity: O(N)
'''