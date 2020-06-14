def flip_bit_to_win(num: int) -> int:
    seqs, cnt_one, mx_len = [], 0, 0
    while num > 0:
        if num & 1:
            cnt_one += 1
        else:
            seqs.append(cnt_one)
            cnt_one = 0
        num >>= 1
    seqs.append(cnt_one)
    for i in range(len(seqs) - 1):
        mx_len = max(seqs[i] + seqs[i + 1] + 1, mx_len)
    return mx_len