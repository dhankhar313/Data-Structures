def linear_search(value, lst):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return None


def time_function(value, lst):
    import time
    t0 = time.time()
    idx = linear_search(value, lst)

    return round(time.time() - t0, 10), idx


if __name__ == '__main__':
    numbers = [i for i in range(10000000)]
    return_values = time_function(5120000, numbers)
    print("Time taken: ", return_values[0])
    print("Number not found in the lst") if return_values[1] is None else print(
        f"Number found at index {return_values[1]}")
