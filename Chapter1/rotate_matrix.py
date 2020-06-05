from typing import List
def rotate_matrix(mat: List[List[int]]) -> List[List[int]]:
    n = len(mat)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            temp = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
            mat[j][n - 1 -i] = mat[i][j]
            mat[i][j] = temp
    return mat
'''
Intuition: Draw few examples, then find the pattern
Time complexity: O(N^2)
Space complexity: O(1)
'''