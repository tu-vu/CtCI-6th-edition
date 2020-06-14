def next_number(n: int) -> str:
    # First 0 bit that has 1 before it 01...
    i = 0
    # Counter to number of 1s before two bits above
    cnt_one = -1
    # Hold previous bit
    prev = None
    res = n
    for _ in range(32):
        cur = n & 1
        # current bit is 0
        if not cur:
            # prev is 1
            if prev:
                break
        else:
            cnt_one += 1
        n >>= 1
        i += 1
        prev = cur
    # Flip that zero and one bit
    res = res ^ (1 << i)
    res = res ^ (1 << i - 1)
    # Clear all bit before two bits above
    res = res & (~0 << i - 1)
    # Add remaining one to end
    res = res ^ ((1 << cnt_one) - 1)
    return bin(res)