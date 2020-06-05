import collections
def is_permutation(s1: str, s2: str) -> bool:
    # If lengths are different, they can't be permutation of each other
    if len(s1) != len(s2):
        return False

    # Declare Counter objects to keep track of freq of each char in string
    cnt1 = collections.Counter(s1)
    cnt2 = collections.Counter(s2)

    for c in cnt1:
        # Check if frequency of char c in s1 and s2 are different
        if cnt1[c] != cnt2[c]:
            return False
    return True
'''
Time complexity:  O(N)
Space complexity: O(1), there are at most 128 ASCII chars so O(128) = O(1)
'''