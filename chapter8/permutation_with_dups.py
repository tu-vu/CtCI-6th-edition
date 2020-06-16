from typing import List
import copy
def permutation_with_dups(word: str) -> List[List[str]]:
    def get_permutation(s: List[str], n: int) -> List[List[int]]:
        if n == 1:
            return [[s[n - 1]]]
        p = get_permutation(s, n - 1)
        cur = []
        for seq in p:
            for i in range(n):
                if i == 0 or seq[i - 1] != s[n - 1]:
                    cpy = copy.deepcopy(seq)
                    cpy.insert(i, s[n - 1])
                    cur.append(cpy)
        return cur
    s = list(word)
    return get_permutation(s, len(s))