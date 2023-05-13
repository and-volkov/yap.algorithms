from typing import List

POSSIBLE_LETTERS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def generate_combinations(buttons: dict, inp_list: List[int]) -> str:
    if len(inp_list) == 1:
        return list(buttons[inp_list[0]])
    else:
        result = []
        for letter in buttons[inp_list[0]]:
            for comb in generate_combinations(buttons, inp_list[1:]):
                result.append(letter + comb)
        return result


if __name__ == '__main__':
    inp = [int(num) for num in input()]
    print(" ".join(generate_combinations(POSSIBLE_LETTERS, inp)))
