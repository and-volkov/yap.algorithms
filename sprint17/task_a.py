def generate_correct_brackets_sequence(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    result = []
    for i in range(n):
        for left in generate_correct_brackets_sequence(i):
            for right in generate_correct_brackets_sequence(n - i - 1):
                result.append(f"({left}){right}")
    return sorted(result)


if __name__ == '__main__':
    n = int(input())
    print('\n'.join(generate_correct_brackets_sequence(n)))
