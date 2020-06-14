def pairwise_swap(n: int) -> str:
    # Get least significant bit
    least_bit = n & 1
    # Assume we are only using 32 bits
    return bin((1 << 32) ^ (n >> 1)) if least_bit else bin(n >> 1)