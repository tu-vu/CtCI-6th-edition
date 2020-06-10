from typing import List
from typing import Dict
import collections
def build_order(projects: List[str], dependencies: List[List[str]]):
    # Declare a bool array that tracks visited nodes to avoid infinite cycle
    visited = collections.defaultdict(bool)

    # Build graph
    g = collections.defaultdict(list)
    for dp in dependencies:
        g[dp[0]].append(dp[1])

    # Depth-first search
    def dfs(g: Dict[str, List[str]], visited: Dict[str, bool]) -> List[str]:
        res = []
        def dfs_visit(g: Dict[str, List[str]], visisted: Dict[str, bool], cur: str) -> List[str]:
            visited[cur] = True
            path = []
            if not cur in g:
                return [cur]
            for neighbor in g[cur]:
                if not visited[neighbor]:
                   # For sibling, append the path in reverse order
                   path = dfs_visit(g, visited, neighbor) + path
            return [cur] + path
        for project in projects:
            if not visited[project]:
                res = dfs_visit(g, visited, project) + res
        return res
    return dfs(g, visited) 
'''
Intuition: Topological sort!
Time complexity: O(V + E)
Space complexity: O(V + E)
'''