def recursive_binary_search(value, list):
    if len(list) == 0:
        return None
    else:
        mid = len(list) // 2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            recursive_binary_search(value, list[mid + 1:])
        else:
            recursive_binary_search(value, list[:mid - 1])


def time_function(function, value, list):
    import time
    t0 = time.time()
    idx = function(value, list)

    return round(time.time() - t0, 10), idx


if __name__ == '__main__':
    numbers = [i for i in range(10000000)]
    return_values = time_function(recursive_binary_search, 5120000, numbers)
    print("Time taken: ", return_values[0])
    # print("Number not found in the list") if return_values[1] is False else print("Number found in the list")
    print("Number not found in the list") if return_values[1] is None else print(
        f"Number found at index {return_values[1]}")
