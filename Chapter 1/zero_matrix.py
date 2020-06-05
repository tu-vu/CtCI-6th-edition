from typing import List
def zero_matrix(mat: List[List[int]]) -> List[List[int]]:
    # Declare 2 HashSet to keep track of zero cols, rows
    zero_col, zero_row = set(), set()
    m, n = len(mat), len(mat[0])

    # First pass to fill the HashSets
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    # Second pass to modify the array based on HashSets
    for i in range(m):
        for j in range(n):
            if i in zero_row or j in zero_col:
                mat[i][j] = 0
    return mat
'''
Time complexity: O(M * N)
Space complexity: O(max(M,N))
'''