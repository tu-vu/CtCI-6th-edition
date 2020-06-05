import collections
def str_compression(s: str) -> str:
    length, res = len(s), ""

    # Initialize a pointer to first char in duplicate sequence
    j = 0

    for i in range(length):
        # Edge case: When we reach last char, append sequence to answer
        if i == length - 1:
            res += s[j] + str(i + 1 - j)
        # If not in sequence, append encoded sequence to answer and reset pointer
        if s[i] != s[j]:
            res += s[j] + str(i - j)
            j = i
    return res if len(res) < length else s
'''
Time complexity: O(N)
Space complexity: O(N) for answer
'''
