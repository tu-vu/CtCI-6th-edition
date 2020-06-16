from typing import List
import copy
def permutation_without_dups(word: str) -> List[List[str]]:
    def get_permutation(s: List[str], n: int) -> List[List[str]]:
        if n == 1:
            return [[s[n - 1]]]
        subsets = get_permutation(s, n - 1)
        cur = []
        for subset in subsets:
            for i in range(n):
                cpy = copy.deepcopy(subset)
                cpy.insert(i, s[n - 1])
                cur.append(cpy)
        return cur
    s = list(word)
    return get_permutation(s, len(s))