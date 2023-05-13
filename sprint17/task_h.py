def compare_str_numbers(a: int, b: int) -> bool:
    return a + b < b + a


def bubble_sort_compare(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if compare_str_numbers(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return ''.join(str(i) for i in arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    print(bubble_sort_compare(arr))