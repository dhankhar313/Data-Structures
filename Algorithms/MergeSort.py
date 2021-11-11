import random
import time


def merge_sort(lst):
    # print('List is: ', lst)
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    # print('called with args: ', left, right)
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1
    return result


def time_function(lst):
    t0 = time.time()
    final = merge_sort(lst)
    return round(time.time() - t0, 10), final


if __name__ == "__main__":
    lst = list(range(10))
    random.shuffle(lst)
    print('Original List: ', lst)
    t, final = time_function(lst)
    print('Time taken to sort list: ', t)
    print('Sorted List: ', final)
