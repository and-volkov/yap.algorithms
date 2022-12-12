from typing import List

n = int(input())
street = list(map(int, input().split()))


def calc_distances(street: List[int], n: int) -> List[int]:
    ans = [0] * n
    max_distance = 10**9
    for fwd in range(n):
        if street[fwd] != 0:
            distance = abs(max_distance - fwd)
            if ans[fwd] > distance or ans[fwd] == 0:
                ans[fwd] = distance
        else:
            max_distance = fwd

    max_distance = 10**9
    for bkwd in range(n - 1, -1, -1):
        if street[bkwd] != 0:
            distance = abs(max_distance - bkwd)
            if ans[bkwd] > distance or ans[bkwd] == 0:
                ans[bkwd] = distance
        else:
            max_distance = bkwd

    return ans


print(' '.join(map(str, calc_distances(street, n))))
# time complexity O(n**2)
# space complexity O(n)
# ID = 79290026
