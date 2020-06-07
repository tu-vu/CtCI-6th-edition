class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

# Iterative version
def sum_lists_iter(h1: Node, h2: Node) -> Node:
    ans, cur, carry = None, None, False
    while h1 or h2 or carry:
        digit1 = h1.val if h1 else 0
        digit2 = h2.val if h2 else 0
        cur_digit = (digit1 + digit2 + carry) % 10
        carry = digit1 + digit2 + carry >= 10
        if cur:
            cur.next = Node(cur_digit)
            cur = cur.next
        else:
            ans = Node(cur_digit)
            cur = ans
        h1 = h1.next if h1 else h1
        h2 = h2.next if h2 else h2
    return ans
'''
Time complexity: O(max(A,B))
Space complexity: O(1)
'''

# Recursive version
def sum_lists_recur(h1: Node, h2: Node) -> Node:
    def helper(h1: Node, h2: Node, carry: bool) -> Node:
        if h1 or h2 or carry:
            digit1 = digit2 = 0
            if h1:
                digit1 = h1.val
                h1 = h1.next
            if h2:
                digit2 = h2.val
                h2 = h2.next
            cur = Node((digit1 + digit2 + carry) % 10)
            carry = digit1 + digit2 + carry >= 10
            cur.next = helper(h1, h2, carry)
            return cur
        return None
    return helper(h1, h2, False)
'''
Time complexity: O(max(A,B))
Space complexity: O(max(A,B)) from stack calls
'''


