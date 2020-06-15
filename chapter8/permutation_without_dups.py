from typing import List
import copy
def permutation_without_dups(word: str) -> List[List[str]]:
    def get_permutation(s: List[str], index: int) -> List[List[str]]:
        if index == 0:
            return [[s[index]]]
        subsets = get_permutation(s, index - 1)
        cur_set = []
        for subset in subsets:
            for i in range(index + 1):
                cpy = copy.deepcopy(subset)
                cpy.insert(i, s[index])
                cur_set.append(cpy)
        return cur_set
    s = list(word)
    return get_permutation(s, len(s) - 1)