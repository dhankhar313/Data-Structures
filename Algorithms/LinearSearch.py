def linear_search(value, list):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return None


def time_function(function, value, list):
    import time
    t0 = time.time()
    idx = function(value, list)

    return round(time.time() - t0, 10), idx


if __name__ == '__main__':
    numbers = [i for i in range(10000000)]
    return_values = time_function(linear_search, 5120000, numbers)
    print("Time taken: ", return_values[0])
    print("Number not found in the list") if return_values[1] is None else print(
        f"Number found at index {return_values[1]}")
