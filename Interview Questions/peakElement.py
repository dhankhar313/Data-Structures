def find_peak(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


def find_peak_recursive(arr, left, right):
    if left >= right:
        return left
    mid = (left + right) // 2
    if arr[mid] < arr[mid + 1]:
        return find_peak_recursive(arr, mid + 1, right)
    else:
        return find_peak_recursive(arr, left, mid)


if __name__ == "__main__":
    arr = [1, 2, 3, 5, 5]
    print(find_peak(arr))
    print(find_peak_recursive(arr, 0, len(arr) - 1))
