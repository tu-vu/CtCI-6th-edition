from typing import List
import collections
def towers_of_hanoi(n: int) -> List[List[int]]:
    towers = [collections.deque() for _ in range(3)]
    towers[0].extend(range(n, 0, -1))
    def move_towers(n: int, src: int, des: int, buff: int, towers: List[List[int]]) -> None:
        if n == 1: # Move top disk to destination
            towers[des].append(towers[src].pop())
        else:
            move_towers(n - 1, src, buff, des, towers)
            # Move top disk to destination
            towers[des].append(towers[src].pop())
            move_towers(n - 1, buff, des, src, towers)
    move_towers(n, 0, 2, 1, towers)
    return towers