import math


def bubbleSort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(lst)


def selectionSort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    print(lst)


def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    # print(lst)
    return lst


def bucketSort(lst):
    num_buckets = round(math.sqrt(len(lst)))
    maxValue = max(lst)
    buckets = []
    for i in range(num_buckets):
        buckets.append([])
    for i in lst:
        idx = math.ceil(i * num_buckets / maxValue)
        buckets[idx - 1].append(i)
    for i in range(num_buckets):
        buckets[i] = insertionSort(buckets[i])
    buckets = [item for sublist in buckets for item in sublist]
    return buckets


if __name__ == '__main__':
    lst = [23, 65, 31, 37, 21, 1, 897, 33, 456, 211]
    # bubbleSort(lst)
    # selectionSort(lst)
    # insertionSort(lst)
    # bucketSort(lst)
    print(bucketSort(lst))
