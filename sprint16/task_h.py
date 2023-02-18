BRACKETS = {")": "(", "]": "[", "}": "{"}


def read_input():
    return input().strip()


def is_correct_bracket_seq(seq: str) -> bool:
    if not seq:
        return True
    if seq[0] in BRACKETS.keys():
        return False
    stack = []
    for bracket in seq:
        if bracket in BRACKETS.values():
            stack.append(bracket)
        elif not stack:
            return False
        elif stack[-1] == BRACKETS[bracket]:
            stack.pop()
        else:
            return False
    return True if not stack else False


if __name__ == "__main__":
    sequence = read_input()
    print(is_correct_bracket_seq(sequence))
