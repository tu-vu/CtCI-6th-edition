from typing import List
import collections
def route_btw_nodes(g: List[List[int]], src: int, des: int) -> bool:
    # Declare a bool array that tracks visited nodes to avoid infinite cycle
    visited = [False] * len(g)
    q = collections.deque()
    visited[src] = True
    q.append(src)
    while q:
        r = q.popleft()
        for neighbor in g[r]:
            if neighbor == des:
                return True
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return False
'''
Time complexity: O(V + E)
Space complexity: O(V)
'''