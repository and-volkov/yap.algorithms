from typing import List, Tuple

SIZE_OF_FIELD = 4


def read_input() -> Tuple[int, List[List[str]]]:
    buttons_count = int(input())
    field = []
    for _ in range(SIZE_OF_FIELD):
        field.append(list(input()))
    return buttons_count, field


def count_win_rounds(buttons_count: int, field: List[List[str]]) -> int:
    symbols = {}
    for row in field:
        for symbol in row:
            if not symbols.get(symbol):
                symbols[symbol] = 0
            symbols[symbol] += 1
    return sum(
        1
        for key in symbols.keys()
        if symbols[key] <= buttons_count * 2 and key != "."
    )


if __name__ == "__main__":
    max_buttons, game_field = read_input()
    print(count_win_rounds(max_buttons, game_field))

# time complexity O(N x M x len(keys)) => O(4 x 4 x 10(max keys)) => O(1)
# space complexity O(10(keys) x 10(values)) => O(1)
# ID = 79440406
