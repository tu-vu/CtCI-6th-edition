from typing import List
def power_set(S: List[int]) -> List[List[int]]:
    def get_subsets(S: List[int], n: int) -> List[List[int]]:
        if n == -1:
            return [[]]
        subsets = get_subsets(S, n - 1)
        cur_set = [s + [S[n]] for s in subsets] + subsets
        return cur_set
    return get_subsets(S, len(S) - 1)
'''
Time complexity: O(n*2^n)
Space complexity: O(n)
'''