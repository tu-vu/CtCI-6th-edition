def insertion(N: int, M: int, i: int, j: int) -> str:
    all_ones = ~0 
    left = all_ones << (j + 1) # 11...1100...00 (j zeros)
    right = (1 << i) - 1       # 00...0011...11 (i ones)
    mask = left | right        # 11...1100...0011...11 (j - i + 1 zeros)
    # Clear all bits from j to i from N
    N = N & mask
    return bin(N | M << i)