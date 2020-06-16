from typing import List
def parens(n: int) -> List[str]:
    if n == 1:
        return ["()"]
    p = parens(n - 1)
    cur = set()
    for seq in p:
        cur.add("(" + seq + ")")
        cur.add("()" + seq)
        cur.add(seq + "()")
    return list(cur)