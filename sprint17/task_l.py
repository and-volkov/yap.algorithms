def recursive_binary_search(data, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target <= data[mid] and not (mid > 0 and target <= data[mid - 1]):
            return mid + 1
        elif target <= data[mid]:
            return recursive_binary_search(data, target, low, mid - 1)
        else:
            return recursive_binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    target = int(input())
    a = recursive_binary_search(data, target, 0, n - 1)
    b = recursive_binary_search(data, target + target, a, n - 1)
    print(a, b)
