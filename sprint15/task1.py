from typing import List


def read_input() -> List[int]:
    _ = input()
    street_map = list(map(int, input().split()))
    return street_map


def calc_distances(street_map: List[int]) -> List[int]:
    ans = [0] * len(street_map)
    max_distance = 10**9
    for forward in range(len(street_map)):
        if street[forward] != 0:  # comment at the end of file
            distance = abs(max_distance - forward)
            if ans[forward] > distance or ans[forward] == 0:
                ans[forward] = distance
        else:
            max_distance = forward

    max_distance = 10**9
    for backward in range(len(street_map) - 1, -1, -1):
        if street[backward] != 0:
            distance = abs(max_distance - backward)
            if ans[backward] > distance or ans[backward] == 0:
                ans[backward] = distance
        else:
            max_distance = backward
    return ans


if __name__ == "__main__":
    street = read_input()
    print(" ".join(map(str, calc_distances(street))))

# time complexity O(n**2)
# space complexity O(n)
# ID = 79442850

# если не конвертить массив на входе, то строка с расстоянием будет другой
# distance = str(abs(int(max_distance) - int(forward))
# получится, что в худшем случае (один ноль на улице)
# я буду конвертить n - 1 чисел 2 раза при каждом проходе
# или я что-то не понимаю?
