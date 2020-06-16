from typing import List
def paint_fill(board: List[List[str]], r: int, c: int, color: str) -> None:
    def paint_cell(board: List[List[str]], r: int, c: int, rows: int, cols: int, color: str) -> None:
        if (r >= rows or r < 0) or (c >= cols or c < 0) or board[r][c] == color:
            return
        board[r][c] = color
        paint_cell(board, r + 1, c, rows, cols, color)
        paint_cell(board, r - 1, c, rows, cols, color)
        paint_cell(board, r, c + 1, rows, cols, color)
        paint_cell(board, r, c - 1, rows, cols, color)
    rows = len(board)
    cols = len(board[0])
    paint_cell(board, r, c, rows, cols, color)
board = [['r' for _ in range(4)] for _ in range(3)]
paint_fill(board, 1, 2, 'b')
print(board)