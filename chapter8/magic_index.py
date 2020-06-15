from typing import List
def magic_index(A: List[int]) -> int:
    def bin_search(A: List[int], lo: int, hi: int) -> int:
        if lo > hi: # Not found!
            return -1
        mid = (lo + hi) // 2
        if A[mid] == mid:
            return mid
        elif A[mid] < mid:
            return bin_search(A, mid + 1, hi)
        else:
            return bin_search(A, lo, mid - 1)
    return bin_search(A, 0, len(A) - 1)
'''
Time complexity: O(logN)
Space complexity: O(logN) from stack calls
'''
