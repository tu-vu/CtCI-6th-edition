import collections
def is_palindrome_permutation(s: str) -> bool:
    # Declare a Counter object to keep track of freq of each char in s
    cnt = collections.Counter(s)

    # Track the number of odd freqs
    cnt_odd = 0

    for c, freq in cnt.items():
        # Skip whitespace
        if c != " " and freq % 2 != 0:
            cnt_odd += 1
    return cnt_odd > 1
'''
Intuition: A palindrome permutation has at most one char with odd freq
Time complexity:  O(N)
Space complexity: O(1), there are at most 128 ASCII chars so O(128) = O(1)
'''
