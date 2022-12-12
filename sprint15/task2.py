SIZE = 4
k = int(input())

def count_win_rounds(k: int) -> int:
    symbols = {}
    for i in range(SIZE):
        for symb in input():
            if not symbols.get(symb):
                symbols[symb] = 0
            symbols[symb] += 1

    return sum(
        1 for key in symbols.keys() if symbols[key] <= k * 2 and key != '.'
    )


print(count_win_rounds(k))
# time complexity O(N x M x len(keys)) => O(4 x 4 x 10(max keys)) => O(1)
# space complexity O(10(keys) x 10(values)) => O(1)
# ID = 79292730
