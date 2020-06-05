import collections
def is_oneaway(s1: str, s2: str) -> bool:
    # Declare Counter objects to keep track of freq of each char in string
    cnt1 = collections.Counter(s1)
    cnt2 = collections.Counter(s2)

    # Keep track of number of common chars
    common_cnt = 0

    for c in cnt1:
        common_cnt += min(cnt1[c], cnt2[c])
    return max(len(s1), len(s2)) - common_cnt <= 1
'''
Time complexity: O(N)
Space complexity: O(1), there are at most 128 ASCII chars so O(128) = O(1)
'''