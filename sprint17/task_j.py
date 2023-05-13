def bubble_sort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                flag = 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag == 0 and i == 0:
            print(*arr)
            return
        if flag == 1:
            print(*arr)
    return arr


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)
