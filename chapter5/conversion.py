def conversion(A: int, B: int) -> int:
    res = 0
    diff_seq = A ^ B
    for _ in range(32):
        res += diff_seq & 1
        diff_seq >>= 1
    return res